
# VISIONS-HOW_TO.md

How to create and write Artsy Visions stories.

## Overview


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

Guidelines for this step are in a separate file named `VISIONS-CONTENT.md` in this directory.

## Step 4. Publish

The name of the newly-published file should have a numerical prefix higher than the others in
the visions directory, so that it will show up at the top of the pages in which it appears.

## Step 5. Deploy

This part of the process is outside the scope of this document.
