#coding: utf-8
#
from fabric.api import task, sudo, run, cd

RUBY_VERSION = "2.1.0"
RBENV_CMD = "~/.rbenv/bin/rbenv"

@task
def provision():
    sudo("apt-get -y update")

    modules = ["build-essential", "git-core"]
    sudo("apt-get install " + " ".join(modules))

    run("git clone https://github.com/sstephenson/rbenv.git ~/.rbenv")
    run("echo 'export PATH=\"$HOME/.rbenv/bin:$PATH\"' >> ~/.bashrc")
    run("echo 'eval \"$(rbenv init -)\"' >> ~/.bashrc")

    run("git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build")

    run("git clone https://github.com/carsomyr/rbenv-bundler.git ~/.rbenv/plugins/bundler")

    run("%s install %s" % (RBENV_CMD, RUBY_VERSION))
    run("%s global %s" % (RBENV_CMD, RUBY_VERSION))

    # [TODO] these steps below need to be done manually for now
    run("sudo gem install bundler --no-ri --no-rdoc")
    run("%s rehash" % RBENV_CMD)

    with cd("~/my-project"):
        run("bundle install")
