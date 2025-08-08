
### Directory with Ansible Collections

```bash
cd ~/.ansible/collections/ansible_collections/
```

### Example Collection Structure

```bash
$ tree -C clay584/
clay584/
└── genie
    ├── FILES.json
    ├── MANIFEST.json
    ├── README.md
    ├── colored_diff.png
    ├── learn_genie_params.png
    └── plugins
        ├── filter
        │   ├── __pycache__
        │   │   └── parse_genie.cpython-311.pyc
        │   └── parse_genie.py
        └── modules
            ├── args.json
            └── learn_genie.py

5 directories, 9 files
```

### Example Collection Installation Process

```bash
$ ansible-galaxy collection install nokia.sros
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/nokia-sros-1.6.0.tar.gz to /home/kbyers/.ansible/tmp/ansible-local-180615c1hpeaas/tmpmgjnm6ce/nokia-sros-1.6.0-zcaad1vm
Installing 'nokia.sros:1.6.0' to '/home/kbyers/.ansible/collections/ansible_collections/nokia/sros'
nokia.sros:1.6.0 was installed successfully
```
