#!/usr/bin/env python3
"""Convert the Grin book from Markdown to EPUB for Kindle."""

import re
from pathlib import Path
from ebooklib import epub

def markdown_to_html(md_text):
    """Convert markdown to HTML."""
    html = md_text

    # Headers
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Blockquotes
    lines = html.split('\n')
    in_blockquote = False
    result = []
    for line in lines:
        if line.startswith('>'):
            if not in_blockquote:
                result.append('<blockquote>')
                in_blockquote = True
            result.append(line[1:].strip())
        else:
            if in_blockquote:
                result.append('</blockquote>')
                in_blockquote = False
            result.append(line)
    if in_blockquote:
        result.append('</blockquote>')
    html = '\n'.join(result)

    # Horizontal rules
    html = re.sub(r'^---+$', r'<hr/>', html, flags=re.MULTILINE)

    # Paragraphs
    paragraphs = html.split('\n\n')
    processed = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('<h') or p.startswith('<blockquote') or p.startswith('<hr'):
            processed.append(p)
        else:
            p = p.replace('\n', ' ')
            processed.append(f'<p>{p}</p>')

    return '\n'.join(processed)


def create_epub():
    book_dir = Path(__file__).parent

    # Create EPUB book
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('grin-story-2025')
    book.set_title('Grin: A Brief Story')
    book.set_language('en')
    book.add_author('Wayne George')
    book.add_metadata('DC', 'description',
        'The development history of Grin cryptocurrency, from the mysterious '
        'MimbleWimble whitepaper to a thriving open-source project.')

    # CSS styling for Kindle
    style = '''
    body {
        font-family: Georgia, serif;
        line-height: 1.6;
        margin: 5%;
    }
    h1 {
        font-size: 1.8em;
        margin-top: 1em;
        margin-bottom: 0.5em;
        page-break-before: always;
    }
    h2 {
        font-size: 1.4em;
        margin-top: 1.2em;
        margin-bottom: 0.4em;
    }
    h3 {
        font-size: 1.2em;
        margin-top: 1em;
        margin-bottom: 0.3em;
    }
    p {
        text-indent: 1.5em;
        margin: 0.5em 0;
        text-align: justify;
    }
    blockquote {
        margin: 1em 2em;
        padding-left: 1em;
        border-left: 3px solid #ccc;
        font-style: italic;
    }
    hr {
        margin: 2em 0;
        border: none;
        border-top: 1px solid #ccc;
    }
    .no-indent {
        text-indent: 0;
    }
    '''

    nav_css = epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style
    )
    book.add_item(nav_css)

    # Read chapter files
    chapters = []
    chapter_files = sorted(book_dir.glob('chapters/*_final.md'))

    chapter_titles = [
        "MimbleWimble Origins",
        "Building in Public",
        "Road to Launch",
        "Launch Day",
        "Growing Pains",
        "First Hard Fork",
        "The Hard Fork Years",
        "Governance Evolution",
        "Decentralized Development",
        "Legacy & Future"
    ]

    for i, chapter_file in enumerate(chapter_files):
        md_content = chapter_file.read_text(encoding='utf-8')
        html_content = markdown_to_html(md_content)

        # Create chapter
        chapter_num = i + 1
        title = chapter_titles[i] if i < len(chapter_titles) else f"Chapter {chapter_num}"

        chapter = epub.EpubHtml(
            title=title,
            file_name=f'chapter_{chapter_num:02d}.xhtml',
            lang='en'
        )
        chapter.content = f'''
        <html>
        <head>
            <title>{title}</title>
            <link rel="stylesheet" type="text/css" href="style/nav.css"/>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        '''
        chapter.add_item(nav_css)
        book.add_item(chapter)
        chapters.append(chapter)

    # Create intro page
    intro = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='en')
    intro.content = '''
    <html>
    <head>
        <title>Introduction</title>
        <link rel="stylesheet" type="text/css" href="style/nav.css"/>
    </head>
    <body>
        <h1>Grin</h1>
        <h2>A Brief Story</h2>

        <p class="no-indent">In July 2016, a mysterious figure using the pseudonym Tom Elvis Jedusor
        dropped a whitepaper into a Bitcoin research IRC channel and vanished. The paper described
        MimbleWimble—a new approach to cryptocurrency that promised both privacy and scalability.</p>

        <p>Two months later, another pseudonymous developer called Igno Peverell began implementing
        the idea. What followed was one of the most remarkable stories in cryptocurrency: a project
        built entirely in the open, without venture capital, without an ICO, without a premine—just
        code, community, and shared values.</p>

        <p>This book tells that story, drawn from the Grin forum archives spanning 2018 to 2025.
        It chronicles the technical debates, the governance experiments, the hard forks, and the
        human drama of building something new.</p>

        <p>The names are mostly pseudonyms. The code is real. The story is ongoing.</p>

        <hr/>

        <p class="no-indent"><em>Compiled from the Grin Community Forum, 2018-2025</em></p>
    </body>
    </html>
    '''
    intro.add_item(nav_css)
    book.add_item(intro)

    # Attribution and licensing page
    attr_md = (book_dir / 'ATTRIBUTION_AND_LICENSING.md').read_text(encoding='utf-8')
    attr_html = markdown_to_html(attr_md)
    attribution = epub.EpubHtml(title='Attribution and Licensing', file_name='attribution.xhtml', lang='en')
    attribution.content = f'''
    <html>
    <head>
        <title>Attribution and Licensing</title>
        <link rel="stylesheet" type="text/css" href="style/nav.css"/>
    </head>
    <body>
        {attr_html}
    </body>
    </html>
    '''
    attribution.add_item(nav_css)
    book.add_item(attribution)

    # Table of contents
    book.toc = [intro] + chapters + [attribution]

    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Spine (reading order)
    book.spine = ['nav', intro] + chapters + [attribution]

    # Write EPUB file
    output_path = book_dir / 'Grin - A Brief Story.epub'
    epub.write_epub(str(output_path), book, {})

    print(f"EPUB created: {output_path}")
    print(f"Chapters: {len(chapters)}")

    return output_path


if __name__ == '__main__':
    create_epub()
