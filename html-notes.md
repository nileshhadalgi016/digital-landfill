# HTML Study Notes

## 1. What is HTML?
- HTML (HyperText Markup Language) is the standard markup language for creating web pages.
- It describes the **structure** and **meaning** of content on a webpage using elements (tags) — not how it looks (that's CSS) or how it behaves (that's JavaScript).
- Browsers parse HTML into a tree called the **DOM (Document Object Model)**, which is what actually gets rendered and what JavaScript manipulates.
- HTML is *not* a programming language — there's no logic, loops, or variables. It's a markup/structuring language.
- Current standard: **HTML5**, maintained by WHATWG/W3C.

---

## 2. Basic Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

- `<!DOCTYPE html>` — tells the browser this is an HTML5 document (triggers "standards mode" rendering instead of quirky legacy rendering). Must be the very first line.
- `<html lang="en">` — root element wrapping all content. The `lang` attribute helps screen readers and search engines.
- `<head>` — metadata (title, links to CSS, meta tags, favicon) — not visible on the page itself.
- `<meta charset="UTF-8">` — sets character encoding so special characters/symbols display correctly. Should be the first thing inside `<head>`.
- `<meta name="viewport" ...>` — essential for responsive design; without it, mobile browsers render the page at desktop width and zoom out.
- `<title>` — text shown in the browser tab and used by search engines.
- `<body>` — the visible content of the page. Only one `<body>` per document.

### Common `<head>` contents
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Short page summary for search engines">
    <title>My Page</title>
    <link rel="icon" href="favicon.ico">
    <link rel="stylesheet" href="style.css">
</head>
```

---

## 3. HTML Elements & Tags

- Most elements have an **opening tag** and a **closing tag**: `<p>text</p>`
- Some are **self-closing** (void elements) and never wrap content: `<br>`, `<img>`, `<hr>`, `<input>`, `<meta>`, `<link>`, `<source>`
- Elements can have **attributes**, written as `name="value"` inside the opening tag: `<a href="https://example.com">Link</a>`
- Elements can be **nested** inside other elements, forming a tree structure — but nesting must not overlap: `<b><i>text</i></b>` is valid, `<b><i>text</b></i>` is not.

| Term | Meaning |
|------|---------|
| Tag | `<p>` |
| Element | `<p>Text</p>` (opening tag + content + closing tag) |
| Attribute | `href="..."` inside a tag |
| Content | Text/other elements between tags |
| Void element | Self-closing, no content/closing tag (`<img>`) |
| Nesting | Placing elements inside other elements |

### Element categories
- **Block-level** elements start on a new line and take up full width by default.
- **Inline** elements sit within a line of text and only take up as much width as needed.
- **Inline-block** (a CSS concept, not HTML) behaves like inline but allows width/height.
(See Section 7 for a full comparison.)

---

## 4. Common Tags Reference

### Text & Headings
| Tag | Purpose |
|-----|---------|
| `<h1>`–`<h6>` | Headings (h1 = largest/most important). Use only one `<h1>` per page, ideally, and don't skip levels (e.g. h1 → h3) — it breaks accessibility/screen-reader navigation. |
| `<p>` | Paragraph |
| `<br>` | Line break (forces a new line without starting a new paragraph) |
| `<hr>` | Horizontal rule / thematic break |
| `<strong>` | Bold, semantically "important" (not just visual bold — screen readers announce it differently) |
| `<em>` | Italic, semantically "emphasized" |
| `<b>` | Bold *visually only*, no semantic importance |
| `<i>` | Italic *visually only*, no semantic importance |
| `<mark>` | Highlighted text |
| `<small>` | Fine print/side comments |
| `<sub>` / `<sup>` | Subscript / superscript |
| `<code>` | Inline code snippet |
| `<pre>` | Preformatted text (preserves whitespace/line breaks) |
| `<blockquote>` | Long quotation (block-level) |
| `<q>` | Short inline quotation |
| `<abbr title="...">` | Abbreviation with tooltip on hover |
| `<span>` | Inline generic container (no semantic meaning, used for styling/scripting hooks) |

> **`<strong>`/`<em>` vs `<b>`/`<i>`**: Visually they look the same by default, but `<strong>` and `<em>` carry meaning for screen readers and SEO. Prefer them over `<b>`/`<i>` unless you truly just want a visual style with no semantic weight.

### HTML Entities (Special Characters)
Some characters have special meaning in HTML and need to be "escaped":

| Character | Entity |
|-----------|--------|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| Non-breaking space | `&nbsp;` |
| © | `&copy;` |
| — | `&mdash;` |

Example: to display `<div>` as text on the page, you'd write `&lt;div&gt;`.

### Links & Media
| Tag | Purpose |
|-----|---------|
| `<a href="...">` | Hyperlink. Can link to pages, anchors (`#section`), emails (`mailto:`), or phone numbers (`tel:`) |
| `<img src="..." alt="...">` | Image (void element — no closing tag) |
| `<video controls>` | Video playback, `controls` shows play/pause UI |
| `<audio controls>` | Audio playback |
| `<source>` | Alternate media file inside `<video>`/`<audio>`/`<picture>` |
| `<iframe src="...">` | Embeds another HTML page/document inside the current one (e.g. YouTube embeds, maps) |
| `<figure>` / `<figcaption>` | Groups an image with its caption |

```html
<figure>
    <img src="cat.jpg" alt="A sleeping cat">
    <figcaption>My cat, asleep as usual.</figcaption>
</figure>

<a href="#section2">Jump to Section 2</a>
<a href="mailto:someone@example.com">Email me</a>
```

### Lists
```html
<!-- Unordered (bulleted) -->
<ul>
    <li>Apples</li>
    <li>Bananas</li>
</ul>

<!-- Ordered (numbered) -->
<ol>
    <li>Step one</li>
    <li>Step two</li>
</ol>

<!-- Description list (term + definition pairs) -->
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
</dl>
```
- Lists can be **nested** by placing a `<ul>`/`<ol>` inside an `<li>`.

### Tables
```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>30</td>
        </tr>
    </tbody>
</table>
```
- `<table>` — wraps the whole table
- `<thead>` / `<tbody>` / `<tfoot>` — semantic grouping of header, body, and footer rows (optional but good practice)
- `<tr>` — table row
- `<th>` — header cell (bold, centered by default)
- `<td>` — standard data cell
- `colspan="2"` / `rowspan="2"` attributes let a cell span multiple columns/rows

### Forms
| Tag | Purpose |
|-----|---------|
| `<form action="..." method="post">` | Wraps input controls; `action` = where data is sent, `method` = GET or POST |
| `<input>` | Generic input — type varies by `type` attribute (see below) |
| `<textarea>` | Multi-line text input |
| `<button>` | Clickable button (`type="submit"`, `"reset"`, or `"button"`) |
| `<select>` / `<option>` | Dropdown menu |
| `<label for="...">` | Label tied to a form control via matching `id` — clicking the label focuses the input |
| `<fieldset>` / `<legend>` | Groups related fields with a caption |

### Common `<input>` types
| `type` value | Renders as |
|--------------|-----------|
| `text` | Single-line text box |
| `password` | Masked text box |
| `email` | Text box with email validation |
| `number` | Numeric spinner |
| `checkbox` | Checkbox |
| `radio` | Radio button (grouped via same `name`) |
| `date` | Date picker |
| `file` | File upload |
| `submit` | Submit button |
| `hidden` | Invisible field (sends data without showing UI) |

### Example form
```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="plan">Plan:</label>
    <select id="plan" name="plan">
        <option value="free">Free</option>
        <option value="pro">Pro</option>
    </select>

    <button type="submit">Submit</button>
</form>
```
- `name` attribute is what gets sent to the server (key), `value`/user input is the value.
- `required`, `placeholder`, `disabled`, `readonly`, `min`/`max` are common validation/UX attributes.

### Structural / Semantic Tags
| Tag | Purpose |
|-----|---------|
| `<div>` | Generic block container |
| `<header>` | Top section of page/section |
| `<footer>` | Bottom section |
| `<nav>` | Navigation links |
| `<main>` | Main content of the page |
| `<section>` | Thematic grouping of content |
| `<article>` | Self-contained content (blog post, news item) |
| `<aside>` | Sidebar/tangential content |

> Using semantic tags (`<header>`, `<nav>`, `<article>`, etc.) instead of generic `<div>`s improves accessibility and SEO — screen readers can jump directly to `<nav>` or `<main>`, and search engines weigh content in `<article>`/`<h1>` more heavily.

### Typical semantic page layout
```html
<body>
    <header>
        <nav>...</nav>
    </header>

    <main>
        <section>
            <h2>Section Title</h2>
            <article>
                <h3>Post Title</h3>
                <p>Post content...</p>
            </article>
        </section>
        <aside>Related links / sidebar</aside>
    </main>

    <footer>
        <p>&copy; 2026 My Site</p>
    </footer>
</body>
```

---

## 5. Attributes You'll See Often

| Attribute | Used On | Purpose |
|-----------|---------|---------|
| `id` | Any element | Unique identifier (must be unique per page) |
| `class` | Any element | Group elements for CSS/JS styling (can repeat, multiple per element) |
| `src` | `<img>`, `<script>`, `<video>` | Source file path/URL |
| `href` | `<a>`, `<link>` | Link destination |
| `alt` | `<img>` | Alternative text — read by screen readers, shown if image fails to load |
| `style` | Any element | Inline CSS (generally best avoided in favor of stylesheets) |
| `target="_blank"` | `<a>` | Open link in new tab (pair with `rel="noopener noreferrer"` for security) |
| `title` | Any element | Tooltip text shown on hover |
| `disabled` | Form elements | Greys out/disables the element |
| `data-*` | Any element | Custom data attributes for JS use, e.g. `data-user-id="42"` |

### `id` vs `class`
- `id` — unique, one per page, used for a single specific element (`#header` in CSS, `getElementById` in JS).
- `class` — reusable across many elements, used for shared styling (`.card` in CSS, `getElementsByClassName`/`querySelectorAll` in JS).

### Data attributes example
```html
<div data-user-id="42" data-role="admin">...</div>
```
```js
element.dataset.userId // "42"
```

---

## 6. Comments
```html
<!-- This is a comment and won't be shown in the browser -->
```

---

## 7. Block vs Inline Elements
- **Block-level**: starts on a new line, takes full width (`<div>`, `<p>`, `<h1>`, `<ul>`)
- **Inline**: stays in line with surrounding content, only as wide as needed (`<span>`, `<a>`, `<strong>`, `<em>`)

---

## 8. Connecting CSS & JavaScript
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    ...
    <script src="script.js"></script>
</body>
```
- CSS is usually linked in `<head>`.
- JavaScript is usually placed at the end of `<body>` (so the page loads first).

---

## 9. Quick Tips to Remember
- Always close your tags (except void elements).
- Use `alt` text on images — good practice + accessibility.
- Prefer semantic tags over generic `<div>` where possible.
- Validate your HTML using [W3C Validator](https://validator.w3.org/) if unsure.
- Indent nested elements for readability.

---

## 10. Accessibility (a11y) Basics
- Always add meaningful `alt` text to images (`alt=""` for purely decorative images, so screen readers skip them).
- Use real buttons (`<button>`) and links (`<a>`), not `<div onclick="...">` — they get keyboard focus and screen-reader semantics for free.
- Keep heading order logical (`h1` → `h2` → `h3`, don't skip levels).
- Use `<label>` for every form input.
- Use `lang` attribute on `<html>` so screen readers use correct pronunciation.
- ARIA attributes (`aria-label`, `aria-hidden`, `role`) can add accessibility info when semantic HTML alone isn't enough — but semantic HTML should be the first choice.

---

## 11. Common Beginner Mistakes
- Forgetting to close tags (or closing them in the wrong order — nesting must be properly closed, innermost first).
- Using `<div>` for everything instead of semantic tags.
- Missing `alt` attributes on images.
- Multiple `<h1>` tags with no clear hierarchy.
- Putting block-level elements inside inline elements (e.g. `<p>` inside `<span>`) — invalid nesting.
- Forgetting the viewport meta tag, causing broken mobile layouts.
- Using `<b>`/`<i>` when `<strong>`/`<em>` is semantically more correct.
- Not using `<label for="id">` — makes forms harder to use for accessibility tech and touch users (clicking label doesn't focus input).

---

## 12. Self-Check Questions
1. What's the difference between `<div>` and `<span>`?
2. Why use `<section>` instead of `<div>`?
3. What does the `alt` attribute do and why does it matter?
4. Name 3 void (self-closing) elements.
5. Where should `<script>` tags usually go and why?
6. What's the difference between `<strong>` and `<b>`?
7. What does the `<!DOCTYPE html>` declaration do?
8. What's the difference between `id` and `class`?
9. Why is the viewport meta tag important?
10. What's wrong with using `<div onclick="...">` instead of `<button>`?
