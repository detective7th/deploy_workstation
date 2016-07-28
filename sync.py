import os
import subprocess
import json

def GitClone(url, dst=""):
    cmd = "git clone git@github.com:" + url + " " + dst
    return subprocess.Popen(cmd, shell = True, stdout = None, stderr = None)

def HgClone(url, dst=""):
    cmd = "hg clone https://bitbucket.org/" + url + " " + dst
    return subprocess.Popen(cmd, shell = True, stdout = None, stderr = None)

user_home = os.path.expanduser("~") + '/';
emacs_dir = user_home + ".emacs.d"
emacs = GitClone("detective7th/emacs.git", emacs_dir)
emacs.wait()

os.chdir(emacs_dir)

copy = subprocess.Popen("cp .emacs ../", shell = True, stdout = None, stderr = None)
copy.wait()

data = json.load(open("clone.json"))
repertories = data["repertories"]

dst = user_home + ".emacs.d/lisp"
os.chdir(dst)

handles = []
for obj in repertories:
    type = obj["type"]
    username = obj["username"]
    repertory = obj["repertory"]
    handle = Non
    if 1 == type:
        handle = GitClone(username + "/" + repertory);
    else:
        handle = HgClone(username + "/" + repertory);

    handles.append(handle)

for handle in handles:
    handle.wait()

os.chdir(dst + "/helm")
make = subprocess.Popen("make", shell = True, stdout = None, stderr = None)
make.wait()

###################################################################################################
os.chdir(user_home);
gitconfig_handle = GitClone("detective7th/gitconfig");
gitconfig_handle.wait();

subprocess.Popen("cp ./gitconfig/.gitconfig ./ && cp ./gitconfig/.gitignore ./");

#######################################################################################################################################
down_load_dir = "/tmp/sync/"
if not os.path.exists(down_load_dir):
    os.mkdir(down_load_dir)

#######################################################################################################################################

os.chdir(down_load_dir)
if not os.path.exists(down_load_dir + "boost_1_61_0.tar.bz2"):
    boost_download = subprocess.Popen("wget -c http://jaist.dl.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.bz2", shell = True, stdout = None, stderr = None)
    boost_download.wait()

boost_tar = subprocess.Popen("tar -xjf boost_1_61_0.tar.bz2", shell = True, stdout = None, stderr = None)
boost_tar.wait()

boost_dir = user_home + "boost_1_61_0"
os.chdir(boost_dir)
bootstrap = subprocess.Popen("./bootstrap.sh && ./b2 && sudo ./b2 install", shell = True, stdout = None, stderr = None, stdin = None)

###################################################################################################################################
os.chdir(down_load_dir)
if not os.path.exists(down_load_dir + "global-6.5.4.tar.gz"):
    gtags_download = subprocess.Popen("wget -c http://tamacom.com/global/global-6.5.4.tar.gz", shell = True, stdout = None, stderr = None)
    gtags_download.wait()

gtags_gz = subprocess.Popen("tar -xvzf global-6.5.4.tar.gz", shell = True, stdout = None, stderr = None)
gtags_gz.wait()

gtags_dir = down_load_dir + "global-6.5.4"
os.chdir(gtags_dir)
gtags_make = subprocess.Popen("./configure && make && sudo make install", shell = True, stdout = None, stderr = None, stdin = None)
gtags_make.wait()

if not os.path.exists(user_home + ".gtags"):
    os.mkdir(user_home + ".gtags")

os.chdir(user_home + ".gtags")
ln = subprocess.Popen("ln -s /usr/local/include usr-local-include && ln -s /usr/include usr-include", shell = True, stdout = None, stderr = None)
ln.wait()

mv_move = subprocess.Popen("sudo mv usr-local-include/boost/thread/detail/move.hpp usr-local-include/boost/thread/detail/move.hpp.bak", shell = True, stdout = None, stderr = None, stdin = None)
mv_hana = subprocess.Popen("sudo mv usr-local-include/boost/hana/detail/concepts.hpp usr-local-include/boost/hana/detail/concepts.hpp.bak", shell = True, stdout = None, stderr = None, stdin = None)
mv_move.wait()
mv_hana.wait()
gtags = subprocess.Popen("gtags -c", shell = True, stdout = None, stderr = None)
gtags.wait()
mv_move_bak = subprocess.Popen("sudo mv usr-local-include/boost/thread/detail/move.hpp.bak usr-local-include/boost/thread/detail/move.hpp", shell = True, stdout = None, stderr = None, stdin = None)
mv_hana_bak = subprocess.Popen("sudo mv usr-local-include/boost/hana/detail/concepts.hpp.bak usr-local-include/boost/hana/detail/concepts.hpp", shell = True, stdout = None, stderr = None, stdin = None)
mv_move_bak.wait()
mv_hana_bak.wait()

bootstrap.wait()

##########################################################################################################################
os.chdir(down_load_dir)
boost_dir_clean = subprocess.Popen("rm -rf boost_1_61_0", shell = True, stdout = subprocess.PIPE)
gtags_dir_clean = subprocess.Popen("rm -rf global-6.5.4", shell = True, stdout = subprocess.PIPE)
#boost_clean = subprocess.Popen("rm boost_1_61_0.tar.bz2", shell = True, stdout = subprocess.PIPE)
#gtags_clean = subprocess.Popen("rm global-6.5.4.tar.gz", shell = True, stdout = subprocess.PIPE)

boost_dir_clean.wait()
gtags_dir_clean.wait()
#boost_clean.wait()
#gtags_clean.wait()

exit(0)
