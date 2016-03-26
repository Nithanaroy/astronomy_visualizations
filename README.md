# Assumptions

Search for the keyword `Assumption` in the code to find all assumptions. Match the unique number below for each assumption to find where exactly in the code this assumption is used.

## Domain Related

Assumptions related to the domain or business logic

- 251020: Each star is separated by ONE blank line
- 251021: Each attribute of the star is on its own line
- 251024: Because of the way the records are updated, if a catalogue is updated say from 'FeH 0.3 [Adamow et al. (2015)]' to 'FeH 0.3 [Adamow et al. (2016)]' a new catalogue is added and the particular composition for that catalogue will still be present with old catalogue in the composition table. For the above example the table composition will have 2 entries, one with 2015 catalogue and one with 2016 Fix: Delete the star completely and add it again. Deleting a star, also deletes the corresponding composition elements, but catalogues are retained as other stars may still use it!

## Code Related

Assumptions related to code and are useful for future developers of this project

- 251022: First column returned from select * is always `id` which is the primary key for this table