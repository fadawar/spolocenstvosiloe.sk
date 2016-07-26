spolocenstvosiloe.sk
====================

Development
-----------
You need: vagrant, ansible, nodejs, npm, bower, gulp

### How to start develop
1. `./start_develop.sh`
2. `cd src/`
3. `npm update`
4. `bower update`
5. `gulp`

### Structure of Django application
`/src/static/` - files from `collectstatic` command

`/src/siloe/static/` - static files for whole site

`/src/siloe/templates/` - base templates for whole site

Provisioning
------------
We use Ansible. Secret information are encrypted with ansible-vault and password file must
be named `.ansible-vault-password.txt`.

#### Provisioning production
**Warning!** Don't forget to run `python manage.py collectstatic` before deployment to production.

```ansible-playbook -i ansible/hosts_production ansible/production.yml```

#### Provisioning staging
```ansible-playbook -i ansible/hosts_vagrant ansible/vagrant.yml```

#### Encrypt file
```ansible-vault encrypt ansible/group_vars/staging/vault.yml```

#### Edit encrypted file
```ansible-vault edit ansible/group_vars/staging/vault.yml```
