from fabric.api import local


def update():
    local('rm prettify.min.js')
    local('rm prettify.min.css')
    local('wget https://github.com/tcollard/google-code-prettify/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    local('cp google-code-prettify-master/bin/prettify.min.js .')
    local('cp google-code-prettify-master/bin/prettify.min.css .')
    local('rm -rf google-code-prettify-master')
