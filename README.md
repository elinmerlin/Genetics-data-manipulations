# Quantori Python Academy final project

The project contains functions to manipulate with the genetics data: 
- To convert DNA sequence to RNA sequence;
- To convert the RNA sequence to a polypeptide;
- To plot the GC-content graph based on the DNA sequence.

To deploy the project from the root folder:

    docker-compose up -d --build

To convert DNA sequence to RNA sequence with the command-line argument which you can specify inplace:

    docker-compose run --rm app /app/convert_dna_to_rna.py 'ATGC'

... or put in a file /data/inputs/dna_sequence.txt (in this case use @ symbol before the path):

    docker-compose run --rm app /app/convert_dna_to_rna.py @/app/data/inputs/dna_sequence.txt

To convert the RNA sequence to a polypeptide:

    docker-compose run --rm app /app/convert_rna_to_protein.py @/app/data/inputs/rna_sequence.txt

To plot the GC-content graph:

    docker-compose run --rm app /app/plot_the_gc_ratio.py @/app/data/inputs/dna_sequence.txt 'example' -s 15

You can specify inputs in a /data/inputs/ directory and find the results of the functions in /data/outputs/.


### The project has unittests.

To test the test_convert_dna_to_rna function:

    docker-compose run --rm app -m unittest /app/tests/test_convert_dna_to_rna.py

To test the test_convert_rna_to_protein function:

    docker-compose run --rm app -m unittest /app/tests/test_convert_rna_to_protein.py

To test the test_plot_the_gc_ratio function:

    docker-compose run --rm app -m unittest /app/tests/test_plot_the_gc_ratio.py

To switch containers off:

    docker-compose down -v
