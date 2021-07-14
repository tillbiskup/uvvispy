========
Metadata
========

Metadata are an essential concept of the `ASpecD framework <https://docs.aspecd.de/>`_ and hence the UVVisPy package. They consist of all the relevant information accompanying a UVVis measurement.

Metadata are stored outside the UVVisPy package in simple yet structured text files that focus on human readability and writability, while retaining machine readability.


.. note::

    Of course, it is completely up to you as a user of the UVVisPy package whether you write metadata files during measurement, particularly given that a normal measurement will take less time than writing such a metadata file from scratch. However, be aware of the fact that these metadata files save much more time (and headaches) afterwards, as you will always have a record helping your memory what exactly you measured (ahd probably even why).

    Nevertheless, the import routines of the UVVisPy package will not rely on metadata files to be present. But this means that some information will simply not be available within your datasets.


Due to its widespread use and because it is easy to write (for human beings!), the `YAML format <https://yaml.org/>`_ will be used to store this information. Below is an example of such a YAML file containing a minimum of information for a dataset:

.. code-block:: yaml

    ---
    format:
      type: UV/vis metadata
      version: 0.1.3

    general:
      start:
        date: 2018-05-13
        time: 11:05:00
      end:
        date: 2018-05-13
        time: 11:06:00
      operator: John Doe
      purpose: temperature dependence
      labbook: loi:42.1001/lb/tb/uvvis/yyyy-mm-dd_id

    sample:
      name: PNDIT2
      id: 42
      solvent: Toluene
      concentration: 0.4 mg/ml
      preparation: 1:25 diluted

    cell:
      manufacturer: Hellma
      type: QS 1.00
      pathlength: 1 mm

    temperature control:
      controlled: True
      temperature: 290 K
      controller: Oxford MercuryITC
      cryostat: Oxford Optistat DN2
      cryogen: LN2

    experiment:
      type: spectrum
      measurement mode: absorption

    spectrometer:
      manufacturer: Shimadzu
      model: UV-1601PC
      software: UV Probe, Version 2.43

    data format:
      raw: Shimadzu SPC
      export: ASCII

    comment: |
      And here some comment - with free text. And as YAML allows for using UTF8 characters, you can use special characters too, such as the nasty German "umlauts": äöü

      Even empty lines are allowed, as long as each line is indented.


