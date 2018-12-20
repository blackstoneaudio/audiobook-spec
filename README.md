# Blackstone Audio Audiobook Spec
Data-oriented audiobook specification suitable for distribution and consumption.

## Background
Blackstone Audio is the largest independent Audiobook publisher in the United States, with over 30 years experience in Audiobook production.

We produce and distribute original content through multiple digital and physical channels, and act as an aggregator for other publishers' content.

To date, we have processed over 115,000 audiobook titles, converting them into several formats and packages for delivery to end-users, libraries and resellers.

## Why a Spec?
We have Apps, Web Players, and distribution agreements. All of these need to know what order play the audio, and how to display it. We need to know if we have all the resources for a book, and that those resources are in-tact.

Our automated Ingestion platforms process ONIX to gather all the metadata for a product. Then we receive Audio deliveries through alternative channels.
Our automated delivery platform aggregates the audio (and associated resources) into appropriate packages.
Our end-user apps (Web, Android, iOS) all need to fetch the audio assets, validate them, and then display them in the correct order for playback.

So it all starts with the publisher - and audio deliveries vary from publisher to publisher.

The only thing that is tentatively agreed on is:

1) Filesystem sort order should match the playback order
2) File names should have a consistent structure for each book
2) All numbers should be equally padded
3) All audio will be of the same format
4) The product identifier must be locatable

Sometimes (but not always) there is some form of 'manifest'. This manifest could be in any format (xml, xls, csv, etc) and there is no agreed standard. For us, this file is simply ignored.

When we redistribution content to other resellers, we adhere to the above agreement in addition to the custom specification laid out by our distribution partner.

## Why try to solve distribution AND consumption?

Distribution and consumption by users share common data points beyond "here's a file, play it".

There are also several 'holes' in the delivery chain that break down with the first delivery.

* There is no way for a publisher to communicate any form of playback order, beyond the filesystem sorting.
* If they have taken the extra time to label the tracks (Chapter 1, Part 3, etc) there is no standard way of ingesting that in order to preserve that work.
* They cannot indicate any contractual obligations regarding the labelling of the audio
* There is no standard way of exchanging additional data about the files (md5, runtime, count) to ensure they are complete
