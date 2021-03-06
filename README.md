# SEO Duplication Cartographer

cartodup - or SEO Duplication Cartographer - is a student project written
in Python 3, which compares pages 2 by 2 and returns their similarity ratio.

NB: This app is intended for **python3** use only.


## Installation

Clone this repo using the command

`$ git clone https://github.com/Falinor/seo-cartographer.git`

or download a ZIP archive and unzip it.

Because this project is a student project, it is not referenced in the
pip registry. In order to install the module locally, go to your
installation folder and run:

`$ python3 setup.py install`

Otherwise, you can untar the tarball located in `dist/` folder and copy files
to the relevant folder on your system, so that the app gets runnable.

The module itself is named *cartodup*. Assuming you are still in the
installation folder, you may run `$ mkdir test && cd test` to create a
directory where you will run the app.


## Running the application

The main goal of the application is to compare pages 2 by 2, displaying
their similarity ratio at the end of the process. The `--file` option
allows one to pass a text file containing URLs to fetch data from.

A sample file is present in `resources/pages.txt`. To test the app, you
may run the following:

`$ cartodup -f <REPO_ROOT>/resources/pages.txt`

This command will run the module and output a CSV file containing
results. You can add any number of resource URLs you want.


## Customization

You can customize the `resources/pages.txt` or create your own one.


## Removal

`$ pip3 uninstall cartodup`


## Testing

To test the application, you may run the following:

`$ python3 setup.py test`

This command will run the tests contained in the `tests/` folder.


## Documentation

You can find additional documentation in `docs/build/html/`.
This is the generated API documentation.


## Author

Andrea Gueugnaut
EPITA - MTI 2017
