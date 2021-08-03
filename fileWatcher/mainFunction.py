from fileWatcher.FileWatcher import *

def laucheFileWatcher(needs):
	needs['core'].addComponent(FileWatcher(needs['socket']))