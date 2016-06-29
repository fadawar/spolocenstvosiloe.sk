#!/usr/bin/env bash

vagrant up
vagrant ssh -c "source /home/vagrant/venv/bin/activate;
                cd /vagrant/src/siloe/;
                python3 manage.py runserver 0.0.0.0:8000;"