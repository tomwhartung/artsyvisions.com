
# VISIONS-HOW_TO.md

How to create and write Artsy Visions stories.

## Overview

### Goals

The goal of these stories is to provide **content marketing.**

- Content marketing of books and videos - affiliate links
- Content marketing of the images - get your portrait at Groja.com

### Directories

An Artsy Visions story, or "vision," is defined entirely by static files.

Following is a list of sub-directories of `Site/content/static/content`
relevant to creating visions:

- `images/visions/groups` - jpg files: images featured in stories about groups
- `images/visions/pairs` - jpg files: images featured in stories about pairs
- `images/visions/person` - jpg files: images featured in stories about individuals

- `json/visions` - json files for published stories
- `json/visions-drafts` - json files for drafts of stories
- `json/visions-templates` - json files serving as story file templates

- `html/groups` - html files: body and footnotes for stories about groups
- `html/pairs` - html files: body and footnotes for stories about pairs
- `html/person` - html files: body and footnotes for stories about individuals

# Process

## Overview of Process

The process calls for creating files in roughly this sequence:

1. Add the image or images
2. Use a template to create the json file in the `visions-drafts` directory
3. Add the story and footnotes files
4. Move the json file from the `visions-drafts` directory to `visions` directory
5. Deploy on server to publish new stories

## Step 1. Images

- Single person images
  - Leave image file name the same as on seeourminds.com
  - No need to create new subdirectory for single images
- Pairs of images
  - Create new subdirectory named `images/visions/pairs/[pair_name]
  - Populate new subdirectory using the same image file names as on seeourminds.com
  - Use gimp to create a new image containing both images side-by-side
- Groups:
  - Create new subdirectory named `images/visions/groups/[team_name]
  - Use the same image file names as on seeourminds.com

## Step 2. Using the Templates

- No first person or links in `card_content_html`
- First person OK but still no links in `card_first_person_html`
- The following fields are optional, fill in values, if desired, just for fun:
  - `author`
  - `date`
  - `disclosure_text`
  - `disclosure_btn_text`

## Step 3. Story and Footnotes

**Note that each article may be the visitor's first exposure to the idea of visualizing a personality.**

### First Person

- Ok in Conclusion or Footnotes **only**
  - With extremely rare exceptions, maybe?
  - If "needed," add a footnote and put the "needed" first person phrase there

### Links

- Use minimal links
  - Save the wikipedia, imdb, youtube, and fan site links for the stories at SeeOurMinds.com
- Affiliate links
  - Use these exclusively, if at all possible
  - Unsure what these will look like at this time
- Links to Groja.com and SeeOurMinds.com - certainly are acceptable
  - **Never duplicate any information already on Groja.com/about - always provide a link instead**
  - Remember the original image page at SeeOurMinds.com is the only place where they can see the score
  - Make adding affiliate links to the linked-to pages at SeeOurMinds.com a high priority

### Format and Content of Visions

#### Introduction

**Always** open with general information:

```html
The image above is a spiritual portrait, or <em>Groja</em>¹, representing the personality of___.
```

```html
The images above are spiritual portraits, or <em>Grojas</em>¹, representing the personalities of ___, ___, and ___.
```

#### Overview

– **What is the big picture revealed by the image or images?**

```html
<p>
These spiritual portraits show how ....
</p>
```

#### Context: Where and When

Set the scene, give the source of the character(s):

- Where they are from (real life, book, film, tv, etc.)
- Where they are now
- What they are doing now

#### Who the Image(s) Represent

Describe what the colors represent in PERSON 1, and give an example
[Describe what the colors represent in PERSON 2, and give an example]
[Describe what the colors represent in PERSON 3, and give an example]

#### People and Groups Only: Compare and Contrast

What do they have in common?
What makes them different from each other?
If they are related, what makes their relationship unique?
Is there anything else interesting and specific to this pair of images?

#### Conclusion

- What have we learned from this image or these images?
- This is probably where we should put the affiliate links.
- Ok to use first person here.

#### Footnotes

**Always** include a brief initial footnote explaining the whole idea and providing a link for more information.

```html
¹ A spiritual portrait or <em>Groja</em> &mdash; for
<strong><u>G</u></strong>raphical
<strong><u>R</u></strong>epresentation
<strong><u>o</u></strong>f
<strong><u>J</u></strong>ungian
<strong><u>A</u></strong>rchetypes &mdash;
is an image representing the personality of a person.
Find essential information about these images on the
<a href='https://www.Groja.com/about' title='Link to the About page at Groja.com' target='_blank'>About</a>
page at
<a href='https://www.Groja.com' title='Link to the Home page at Groja.com' target='_blank'>Groja.com</a>.
```

Add other footnotes as appropriate, e.g., for ideas that "need" to be expressed in the first person.

## Step 4. Publish

The name of the newly-published file should have a numerical prefix higher than the others in
the visions directory, so that it will show up at the top of the pages in which it appears.

## Step 5. Deploy

This part of the process is outside the scope of this document.
