# author: 龚潇颖(Xiaoying Gong)
# date： 2019/9/14 15:56  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
import os
import getpass
import shutil

def copy_files(src_dir, dest_dir):
    """
    从一个文件夹中复制文件到另一个文件夹
    :param src_dir:
    :param dest_dir:
    """
    files = os.listdir(src_dir)
    for file in files:
        temp = src_dir + '/' + file
        shutil.copy(temp, dest_dir)


def rename_files(src_dir, dest_dir):
    """
    重命名文件夹中的文件
    :param src_dir:
    :param dest_dir:
    """
    files = os.listdir(src_dir)
    for file in files:
        temp = src_dir + '/' + file
        os.rename(temp, temp+'.jpg')

def del_files(src_dir):
    """
    删除目标文件夹下的所有文件/没有递归删除文件的能力
    :param src_dir:
    :return:
    """
    files = os.listdir(src_dir)
    for file in files:
        os.remove(src_dir + file)

os_user_name = getpass.getuser()
path = r'C:/Users/' + os_user_name + r'/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'
destination = r'F:/myTest/windows聚焦壁纸/temp/'
del_files(destination)
copy_files(path, destination)
rename_files(destination, destination)

