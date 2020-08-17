# ssdmf2csv

Converts the SSA Death Master File to CSV

## FAQ

**Q:** What is the DMF?

**A:** The Death Master File is a database made available for access by the Social Security Administration (SSA) via the National Technical Information Service (NTIS) since 1980, and to this very day. It contains a line-separated list of persons who have had a death reported to the agency from 1962 to the present in a positional format that's painful to work with.

**Q:** What can you do with this data?

**A:** A lot of things, but OSINT, fraud detection, and geneaology are a handful of possible relevant domains.

**Q:** Where can I find the dataset to feed into this script?

**A:** You can pay the NTIS for access (~$3,000/yr), but since the redistribution of the dataset is unrestricted after the fact, you can likely find a slightly outdated copy via your preferred search engine.

**Q:** Why does this script look so terrible?

**A:** This is something that you should not be running more than once. All you should care about is the script working, and the end result being acceptable for your use case. For reference, it took 20 minutes to run through ~11 million rows on an ancient laptop. As a result, there was no need to overengineer this. The only requirement was to be able to get through the file, and properly adhere to this format:

~[format](format.png)


**Q:** What considerations did you take in making this?

**A:** Here's a summary:

    1. Add/change/deletes were ignored.

    2. Since there was chronic inconsistencies in suffixes being in the LAST NAME or NAME SUFFIX, they've been split apart and lumped together into `last_name`

    3. Certain reported death dates will have a day of `00`. Any occurrences of this are left blank.

    4. Everyone gets into fistfights regarding how dates should be formatted, so I've split them all off into their respective columns for your own reconstruction.

Altogether, this should result in a smaller csv that's easier to manage (at least, for most use cases). If you disagree, please feel free to open a pull request!