# Blackstone Audio Audiobook Spec

Data-oriented audiobook specification suitable for distribution and consumption.

Notes can be found in [draft.yaml](draft.yaml)

## Background

Blackstone Audio is the largest independent audiobook publisher in the United States, with 30+ years experience in Audiobook production.

We produce and distribute original content through multiple digital and physical channels, and act as an aggregator for other publishers' content.

To date, we have processed over 115,000 audiobook titles, converting them into several formats and packages for delivery to end-users, libraries and resellers.

## Where does it start?

It all starts with the publisher - and audio deliveries vary from publisher to publisher.

The only things generally agreed are:

* Filesystem sort order should match the playback order
* File names should have a consistent structure for each book
* All numbers should be equally padded
* All audio will be of the same format
* The product identifier must be locatable

Sometimes (but not always) there is some form of 'manifest'. This manifest could be in any format (xml, xls, csv, etc) and there is no agreed standard. For us, this file is simply ignored.

When we redistribute content to other resellers, we adhere to the above agreement in addition to the custom specification laid out by our distribution partner.

## Why a Spec?

ONIX is a fantastic (if complex) standard for communicating metadata. Supplemental material, samples, and cover image URLs can also be included.

Unfortunately ONIX is not suitable for the audio details, and no such standard exists.

We have apps, web players, and distribution agreements. All of these need to know the display and playback order, if we have all the resources for a book, and that those resources are in-tact.

Our automated ingestion platforms process ONIX to gather all the metadata for a product. Then we receive Audio deliveries through alternative channels.

Our automated delivery platform aggregates the audio (and associated resources) into appropriate packages for delivery to resellers and distribution partners.

Through our consumer website we sell content from every major publisher. We offer M4B and zipped MP3s for our customers to download. In addition our apps (web, Android, iOS) play high quality M4As.

## Why try to solve distribution AND consumption?

Distribution and consumption by users share common data points beyond "here's a file, play it".

There are also several 'holes' in the delivery chain that break down with the first delivery.

* There is no way for a publisher to communicate any form of playback order (beyond filesystem sorting).
* If a publisher has taken the extra time to label the tracks (Chapter 1, Part 3, etc) there is no standard way of ingesting that in order to preserve that work.
* Publishers cannot indicate any contractual obligations regarding the labelling of the audio
* There is no standard way of exchanging additional data about the files (md5, runtime, count) to ensure they are complete

## Why YAML? Why not just use 'X'?

* YAML is easy to read
* YAML is a superset of JSON
* YAML supports comments
* YAML supports anchors/aliases
* YAML serializes to JSON

As for 'X':

* Did I mention YAML serializes to JSON?
* XML hurts my eyes
* CSV is not multi-dimensional

## But this "spec" is just a file? Where's the rest?

I believe a single file can describe where the assets are, and how to organize them. Think of it like a packing slip and assembly guide in one.

We could deliver *just* this file (for example to our app) and it would be able to assemble the pieces from cloud storage.
We could include this file in a packaged bundle (ISO, Zip, gZip, Tar etc) and it would equally describe the contents of that package.

## What about M4Bs?

If you are wondering why I would completely ignore M4Bs....

* It's an extension of the MP4 spec, with custom Atoms
* Software options for automated creation is woefully limited
* Software options for playback is equally limited
* A maximum runtime of 9 hours 15 minutes - our average book is 10 hours
* The longer the book the harder it is to navigate
* The 'bookmarks' are flat with no display options
* Only AAC encoded audio is supported
* No support for supplemental material (PDFs, Text Files, etc)
* Audio must be encoded as a single file
* and more....