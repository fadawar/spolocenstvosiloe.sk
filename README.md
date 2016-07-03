spolocenstvosiloe.sk
====================

Development
-----------
You need: nodejs, npm, bower, gulp

Provisioning
------------
We use Ansible. Secret information are encrypted with ansible-vault and password file must
be named ``.ansible-vault-password.txt``.

#### Provisioning production
```ansible-playbook -i ansible/hosts_production ansible/production.yml```

#### Provisioning staging
```ansible-playbook -i ansible/hosts_vagrant ansible/vagrant.yml```

#### Encrypt file
```ansible-vault encrypt ansible/group_vars/staging/vault.yml```

#### Edit encrypted file
```ansible-vault edit ansible/group_vars/staging/vault.yml```
