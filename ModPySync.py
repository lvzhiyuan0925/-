import requests
import time
import os
import src
from src import folder_operations as 模块_1_os
import shutil
import zipfile
import commentjson
import random
from plyer import notification
from src import UpdateChecker,app_version





with open('config.json','r',encoding='utf-8') as config:
    config_data = commentjson.load(config)
    configs = config_data.get('configs',{})
    app_settings = config_data.get('app_settings',{})
    # ———————————————————————————————————————————————————
    url = configs.get('url')
    path = configs.get('path_1')
    path_2 = configs.get('path_2')
    path_3 = configs.get('path_3')
    sleep = configs.get('sleep')
    sleep_time = configs.get('sleep_time')
    _notification = configs.get('notification')
    # ———————————————————————————————————————————————————
    changelog = app_settings.get('changelog')
    # ———————————————————————————————————————————————————
    print(f'-软件信息-\nversion:{app_version.__version__}\nchangelog:{changelog}\n\n-配置-\nurl = {url}\npath_1 = {path}\npath_2 = {path_2}\npath_3 = {path_3}\nsleep = {sleep}\nsleep_time = {sleep_time}\nnotification = {_notification}\n——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n使用install -up进行下载最新源码/更新应用')
c_2 = None
str_1 = None
def sasa():
    global path,c_2,path_3,path_2,str_1,sleep,sleep_time,_notification

    if path_2 is None and path_3 is None:
        if str_1 is not None:
            print(f'正在解压{c_2}到{path}')
            zip_file_path = f'{path}/{c_2}'
            extract_path = f'{path}'

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            # 获取顶层文件夹的路径
            top_folder = os.path.commonprefix(zip_ref.namelist())
            print(f'正在移动解压后的文件夹的文件（默认解压会创建一个文件夹）')
            # 移动文件到指定目录
            for item in os.listdir(os.path.join(extract_path, top_folder)):
                s = os.path.join(extract_path, top_folder, item)
                d = os.path.join(extract_path, item)
                shutil.move(s, d)
                print(f'已移动{item}到{d}')

            # 删除原始的顶层文件夹
            shutil.rmtree(os.path.join(extract_path, top_folder))
            print(f'正在删除{str_1}')
            if sleep:
                time.sleep(sleep_time)
            try:
                os.remove(fr'{path}/{str_1}')
                print(f"文件 '{str_1}' 成功删除。")
            except FileNotFoundError:
                print(f"文件 '{str_1}' 不存在。")
            except PermissionError:
                print(f"权限错误：无法删除 '{str_1}'。")
            except Exception as eeeeeeeeeeeeeeeee:
                print(f"发生错误：{eeeeeeeeeeeeeeeee}")
            print('删除移动后的空文件夹...')
            if sleep:
                time.sleep(sleep_time)
            if _notification:
                notification.notify(
                    title='完成',
                    message='！！！！！！！！！',
                    app_name='ModPySync',
                    timeout=60
                )
            print("\033[91m✔完成\033[0m")
            print("\033[92m✔完成\033[0m")
            print("\033[93m✔完成\033[0m")
            print("\033[94m✔完成\033[0m")
            print("\033[95m✔完成\033[0m")
            print("\033[96m✔完成\033[0m")
            print("\033[97m✔完成\033[0m")
            return
        print(f'正在解压{c_2}到{path}')
        zip_file_path = f'{path}/{c_2}'
        extract_path = f'{path}'

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        # 获取顶层文件夹的路径
        top_folder = os.path.commonprefix(zip_ref.namelist())
        print(f'正在移动解压后的文件夹的文件（默认解压会创建一个文件夹）')
        # 移动文件到指定目录
        for item in os.listdir(os.path.join(extract_path, top_folder)):
            s = os.path.join(extract_path, top_folder, item)
            d = os.path.join(extract_path, item)
            shutil.move(s, d)
            print(f'已移动{item}到{d}')

        # 删除原始的顶层文件夹
        shutil.rmtree(os.path.join(extract_path, top_folder))
        print('删除移动后的空文件夹...')
        if sleep:
            time.sleep(sleep_time)
        if _notification:
            notification.notify(
                title='完成',
                message='！！！！！！！！！',
                app_name='ModPySync',
                timeout=60
            )
        print("\033[91m✔完成\033[0m")
        print("\033[92m✔完成\033[0m")
        print("\033[93m✔完成\033[0m")
        print("\033[94m✔完成\033[0m")
        print("\033[95m✔完成\033[0m")
        print("\033[96m✔完成\033[0m")
        print("\033[97m✔完成\033[0m")
    elif path_2 is not None and path_3 is None:
        print(f'正在解压{c_2}到{path}，{path_2}')
        zip_file_path = f'{path}/{c_2}'
        extract_path = f'{path}'
        extract_path_2 = f'{path_2}'

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        with zipfile.ZipFile(zip_file_path,'r') as zip_ref_2:
            zip_ref_2.extractall(extract_path_2)
        # 获取顶层文件夹的路径
        top_folder = os.path.commonprefix(zip_ref.namelist())
        top_folder_2 = os.path.commonprefix(zip_ref_2.namelist())
        print(f'正在移动解压后的文件夹的文件（默认解压会创建一个文件夹）')
        # 移动文件到指定目录
        for item in os.listdir(os.path.join(extract_path, top_folder)):
            s = os.path.join(extract_path, top_folder, item)
            d = os.path.join(extract_path, item)
            shutil.move(s, d)
            print(f'已移动{item}到{d}')

        # 删除原始的顶层文件夹
        shutil.rmtree(os.path.join(extract_path, top_folder))
        print('删除移动后的空文件夹...')
        for item_2 in os.listdir(os.path.join(extract_path_2, top_folder_2)):
            s_2 = os.path.join(extract_path_2, top_folder_2, item_2)
            d_2 = os.path.join(extract_path_2, item_2)
            shutil.move(s_2, d_2)
            print(f'已移动{item_2}到{d_2}')
        print('删除移动后的空文件夹...')
        shutil.rmtree(os.path.join(extract_path_2, top_folder_2))
        if sleep:
            time.sleep(sleep_time)
        if _notification:
            notification.notify(
                title='完成',
                message='！！！！！！！！！',
                app_name='ModPySync',
                timeout=60
            )
        print("\033[91m✔完成\033[0m")
        print("\033[92m✔完成\033[0m")
        print("\033[93m✔完成\033[0m")
        print("\033[94m✔完成\033[0m")
        print("\033[95m✔完成\033[0m")
        print("\033[96m✔完成\033[0m")
        print("\033[97m✔完成\033[0m")
    elif path_3 is not None and path_2 is None:
        print('无法检测config.json   path_2 and path_3')
        while True:
            pass
    elif (path_3 is not None) and (path_2 is not None) and (path is not None):
        print(f'正在解压{c_2}到{path}，{path_2}')
        zip_file_path = f'{path}/{c_2}'
        extract_path = f'{path}'
        extract_path_2 = f'{path_2}'
        extract_path_3 = f'{path_3}'

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref_2:
            zip_ref_2.extractall(extract_path_2)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref_3:
            zip_ref_3.extractall(extract_path_3)
        # 获取顶层文件夹的路径
        top_folder = os.path.commonprefix(zip_ref.namelist())
        top_folder_2 = os.path.commonprefix(zip_ref_2.namelist())
        top_folder_3 = os.path.commonprefix(zip_ref_3.namelist())
        print(f'正在移动解压后的文件夹的文件（默认解压会创建一个文件夹）')
        # 移动文件到指定目录
        for item in os.listdir(os.path.join(extract_path, top_folder)):
            s = os.path.join(extract_path, top_folder, item)
            d = os.path.join(extract_path, item)
            shutil.move(s, d)
            print(f'已移动{item}到{d}')

        # 删除原始的顶层文件夹
        shutil.rmtree(os.path.join(extract_path, top_folder))
        print('删除移动后的空文件夹...')
        for item_2 in os.listdir(os.path.join(extract_path_2, top_folder_2)):
            s_2 = os.path.join(extract_path_2, top_folder_2, item_2)
            d_2 = os.path.join(extract_path_2, item_2)
            shutil.move(s_2, d_2)
            print(f'已移动{item_2}到{d_2}')

        shutil.rmtree(os.path.join(extract_path_2, top_folder_2))
        print('删除移动后的空文件夹...')

        for item_3 in os.listdir(os.path.join(extract_path_3, top_folder_3)):
            s_3 = os.path.join(extract_path_3, top_folder_3, item_3)
            d_3 = os.path.join(extract_path_3, item_3)
            shutil.move(s_3, d_3)
            print(f'已移动{item_3}到{d_3}')

        shutil.rmtree(os.path.join(extract_path_3, top_folder_3))
        print('删除移动后的空文件夹...')
        if sleep:
            time.sleep(sleep_time)

        if _notification:
            notification.notify(
                title='完成',
                message='！！！！！！！！！',
                app_name='ModPySync',
                timeout=60
            )
        print("\033[91m✔完成\033[0m")
        print("\033[92m✔完成\033[0m")
        print("\033[93m✔完成\033[0m")
        print("\033[94m✔完成\033[0m")
        print("\033[95m✔完成\033[0m")
        print("\033[96m✔完成\033[0m")
        print("\033[97m✔完成\033[0m")



def sss(user_input):
    global s,url,path,c_2,str_1,sleep,config_data,sleep_time,_notification
    try:
        command = user_input[0].lower()
        command_2 = [arg.split()[0].lower() for arg in user_input[1:2]]
        command_3 = [arg.split()[0].lower() for arg in user_input[2:3]]
        command_4 = [arg.split()[0].lower() for arg in user_input[3:4]]
        command_5 = [arg.split()[0].lower() for arg in user_input[4:5]]
        command_6 = [arg.split()[0].lower() for arg in user_input[5:6]]
        command__2 = ' '.join(command_2)
        command__3 = ' '.join(command_3)
        command__4 = ' '.join(command_4)
        command__5 = ' '.join(command_5)
        command__6 = ' '.join(command_6)
        if command == 'help':
            print(f'没做好')
        elif command == 'install':
            if command__3 == '-a':
                print('已识别 -a')
                if command__4.isspace():
                    print('请填写必要参数4')
                elif command__4 == '':
                    print('请填写必要参数4')
                elif not command__4:
                    print('请填写必要参数4')
                else:
                    str_1 = command__4
                    print(command__2)
                    if sleep:
                        time.sleep(sleep_time)
                    print('正在删除旧mod(不会删除文件夹)')
                    if sleep:
                        time.sleep(sleep_time)
                    if path_2 is None and path_3 is None:
                        模块_1_os.删除文件夹中的所有文件(path)
                    elif path_2 is not None and path_3 is None:
                        模块_1_os.删除文件夹中的所有文件(path_2)
                        模块_1_os.删除文件夹中的所有文件(path)
                    elif (path_3 is not None) and (path_2 is not None) and (path is not None):
                        模块_1_os.删除文件夹中的所有文件(path_3)
                        模块_1_os.删除文件夹中的所有文件(path_2)
                        模块_1_os.删除文件夹中的所有文件(path)
                    else:
                        print('程序目前不支持这种读取方法，请退出程序解决后重新启动')
                        while True:
                            pass
                    print('正在下载...')
                    c_2 = ' '.join(command_2)
                    try:

                        response = requests.get(f'{url}', verify=True)

                        with open(f'{path}/{c_2}', 'wb') as eee:
                            print(f'正在安装{eee}')
                            eee.write(response.content)

                        print(f'安装成功{eee} 到 {path}文件夹')
                        sasa()
                    except requests.exceptions.RequestException as eeeeee:
                        print(f'无法连接：\n原因：{eeeeee}\n请尝试手动连接：\n{url}')
            elif command__2 == '-b':
                print('换源将删除注释\n确定/取消(Y/N)')
                user_input_2 = input('确定/取消(Y/N)>>>')
                if user_input_2 in ['确定','Y','y']:
                    print('正在换源...')
                    config_data['url'] = str(command__3)
                    with open('config.json', 'w') as file:
                        # 将修改后的 Python 对象写回 JSON 文件
                        commentjson.dump(config_data, file, indent=4)
                        print('成功换源')
                elif user_input_2 in ['取消', 'N', 'n']:
                    print('已取消')
                else:
                    print('已取消')
            elif command__2 == '-up':
                print('检查软件更新中...')
                UpdateChecker.Update()
                user_input_2 = input('确定/取消(Y/N)>>>')
                if user_input_2 in ['确定', 'Y', 'y']:
                    print('正在制作')
                elif user_input_2 in ['取消', 'N', 'n']:
                    print('已取消')
                else:
                    print('已取消')


            else:
                print(' '.join(command_2))
                if sleep:
                    time.sleep(sleep_time)
                print('正在删除旧mod(不会删除文件夹)')
                if sleep:
                    time.sleep(sleep_time)
                if path_2 is None and path_3 is None:
                    模块_1_os.删除文件夹中的所有文件(path)
                elif path_2 is not None and path_3 is None:
                    模块_1_os.删除文件夹中的所有文件(path_2)
                    模块_1_os.删除文件夹中的所有文件(path)
                elif (path_3 is not None) and (path_2 is not None) and (path is not None):
                    模块_1_os.删除文件夹中的所有文件(path_3)
                    模块_1_os.删除文件夹中的所有文件(path_2)
                    模块_1_os.删除文件夹中的所有文件(path)
                else:
                    print('程序目前不支持这种读取方法，请退出程序解决后重新启动')
                    while True:
                        pass
                print('正在下载...')
                c_2 = ' '.join(command_2)
                try:

                    response = requests.get(f'{url}', verify=True)
                    with open(f'{path}/{c_2}','wb') as eee:
                        print(f'正在安装{eee}')
                        eee.write(response.content)

                    print(f'安装成功{eee} 到 {path}文件夹')
                    sasa()
                except requests.exceptions.RequestException as eeeeee:
                    print(f'无法连接：\n原因：{eeeeee}\n请尝试手动连接：\n{url}')
        else:
            print(f'“{command}”不是命令，请检查拼写、软件更新')
    except IndexError:
        pass

while True:
    abc = random.randint(1, 7)
    abc_2 = os.getcwd()
    try:
        s = input(f'\033[9{abc}m{abc_2}>>>\033[0m').split()
        sss(s)
    except (KeyboardInterrupt,UnicodeDecodeError):
        pass