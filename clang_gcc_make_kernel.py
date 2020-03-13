# -*- coding: utf-8 -*-
import os
import time
import platform
from multiprocessing import cpu_count
print("系统处理器为%s个，正在检测脚本路径。。"%(cpu_count()))
a=platform.version()
if "Ubuntu" in a:
    if "18" or "19" in a:
        pypath=os.getcwd()
        if pypath == "/root" :
            xuanzhe=int(input("请务必将所需编译的源码或源码压缩包以及内核补丁放置/root目录下，否则会导致出错！！\n请选择需要的选项：\n1.clang环境安装编译，若已经安装完毕无需再次运行！！！\n2.gcc环境安装，gcc工具链下载。\n3.内核配置修改。\n4.使用clang编译内核。\n5.使用gcc编译内核。\n6.高通clang工具链下载(适用小米官方内核4.14+需首先执行第2项将环境部署完毕)。\n7.高通clang编译内核(适用小米官方内核4.14+)。\n8.内核文件打包为zip\n"))
            if xuanzhe == 1:
                time_start=time.time()
                os.system("sudo apt update")
                os.system("sudo apt install -y bc build-essential ncurses* ncurses-dev libncurses5-dev bzip2 device-tree-compile -y")
                os.system("sudo apt install -y bc build-essential ncurses* ncurses-dev libncurses5-dev bzip2 -y")
                os.system("sudo apt install bison build-essential curl flex git gnupg gperf liblz4-tool libncurses5-dev libsdl1.2-dev libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev -y")
                os.system("sudo apt install g++-multilib gcc-multilib lib32ncurses5-dev lib32z1-dev -y")
                os.system("sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev libesd-java lib32readline-dev lib32readline6 -y")
                os.system("sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev libesd-java lib32readline-dev lib32readline7 -y")
                os.system("sudo apt install python -y")
                os.system("sudo apt install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev -y")
                os.system("sudo apt install git ccache automake flex lzop bison gperf build-essential zip curl zlib1g-dev zlib1g-dev:i386 g++-multilib python-networkx libxml2-utils bzip2 libbz2-dev libbz2-1.0 libghc-bzlib-dev squashfs-tools pngcrush schedtool dpkg-dev liblz4-tool make optipng maven libssl-dev pwgen libswitch-perl policycoreutils minicom libxml-sax-base-perl libxml-simple-perl bc libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev libgl1-mesa-dev xsltproc unzip -y")
                os.system("sudo apt install git ccache automake flex lzop bison   gperf build-essential zip curl zlib1g-dev zlib1g-dev:i386   g++-multilib python-networkx libxml2-utils bzip2 libbz2-dev   libbz2-1.0 libghc-bzlib-dev squashfs-tools pngcrush   schedtool dpkg-dev liblz4-tool make optipng maven libssl-dev   pwgen libswitch-perl policycoreutils minicom libxml-sax-base-perl   libxml-simple-perl bc libc6-dev-i386 lib32ncurses5-dev   x11proto-core-dev libx11-dev lib32z-dev libgl1-mesa-dev xsltproc unzip   mosh htop lsof screen -y")
                os.system("sudo apt install ninja-build bison ca-certificates ccache clang cmake curl file flex gcc g++ git make ninja-build python3 texinfo zlib1g-dev lld -y")
                os.system("mkdir /root/tools")
                os.system("git clone https://github.com/maozhifeng/tc-build.git /root/tools/tc-build")
                os.system("git clone https://gitee.com/mao_zhifeng_admin/binutils-gdb.git /root/tools/tc-build/binutils")
                os.system("git clone https://gitee.com/mao_zhifeng_admin/llvm-project.git /root/tools/tc-build/llvm-project")
                os.system("git clone https://git.kernel.org/pub/scm/utils/dtc/dtc.git /root/tools/dtc-1.4.6 -b v1.4.6")
                os.chdir("/root/tools")
                os.system("make -C dtc-1.4.6 NO_PYTHON=1")
                print("需要的文件已经下载完成，正在编译中，请耐心等待编译完成！")
                os.chdir("/root/tools/tc-build")
                os.system("./build-tc.sh")
                time_end=time.time()
                usetime1=int(time_end-time_start)
                os.system("依赖安装完毕，clang工具链编译完成，本次搭建耗时%s秒"%(usetime1))
                os.chdir("/root/")
                os.system("python3 clang_gcc_make_kernel.py")
            if xuanzhe == 2:
                time_start=time.time()
                os.system("sudo apt update")
                os.system("sudo apt install -y bc build-essential ncurses* ncurses-dev libncurses5-dev bzip2 device-tree-compile -y")
                os.system("sudo apt install -y bc build-essential ncurses* ncurses-dev libncurses5-dev bzip2 -y")
                os.system("sudo apt install bison build-essential curl flex git gnupg gperf liblz4-tool libncurses5-dev libsdl1.2-dev libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev -y")
                os.system("sudo apt install g++-multilib gcc-multilib lib32ncurses5-dev lib32z1-dev -y")
                os.system("sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev libesd-java lib32readline-dev lib32readline6 -y")
                os.system("sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev libesd-java lib32readline-dev lib32readline7 -y")
                os.system("sudo apt install python -y")
                os.system("sudo apt install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev -y")
                os.system("sudo apt install git ccache automake flex lzop bison gperf build-essential zip curl zlib1g-dev zlib1g-dev:i386 g++-multilib python-networkx libxml2-utils bzip2 libbz2-dev libbz2-1.0 libghc-bzlib-dev squashfs-tools pngcrush schedtool dpkg-dev liblz4-tool make optipng maven libssl-dev pwgen libswitch-perl policycoreutils minicom libxml-sax-base-perl libxml-simple-perl bc libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev libgl1-mesa-dev xsltproc unzip -y")
                os.system("sudo apt install git ccache automake flex lzop bison   gperf build-essential zip curl zlib1g-dev zlib1g-dev:i386   g++-multilib python-networkx libxml2-utils bzip2 libbz2-dev   libbz2-1.0 libghc-bzlib-dev squashfs-tools pngcrush   schedtool dpkg-dev liblz4-tool make optipng maven libssl-dev   pwgen libswitch-perl policycoreutils minicom libxml-sax-base-perl   libxml-simple-perl bc libc6-dev-i386 lib32ncurses5-dev   x11proto-core-dev libx11-dev lib32z-dev libgl1-mesa-dev xsltproc unzip   mosh htop lsof screen -y")
                os.system("mkdir /root/tools/google-android-gcc")
                os.chdir("/root/tools/google-android-gcc")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9.git -b marshmallow-release marshmallow-aarch64")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9.git -b nougat-release nougat-aarch64")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9.git -b  oreo-release oreo-aarch64")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9.git -b pie-release pie-aarch64")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9.git -b android10-release android10-aarch64")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.9.git -b marshmallow-release marshmallow-arm")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.9.git -b nougat-release nougat-arm")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.9.git -b  oreo-release oreo-arm")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.9.git -b pie-release pie-arm")
                os.system("git clone https://mirrors.ustc.edu.cn/aosp/platform/prebuilts/gcc/linux-x86/arm/arm-linux-androideabi-4.9.git -b android10-release android10-arm")
                time_end=time.time()
                usetime5=int(time_end-time_start)
                os.system("依赖安装完毕，gcc工具链下载完成，本次耗时%s秒"%(usetime5))
                os.chdir("/root/")
                os.system("python3 clang_gcc_make_kernel.py")
            elif xuanzhe == 3:
                kerneldir=str(input("请输入您内核源码所在文件夹名称:\n"))
                defconfig=str(input("请输入您内核的配置文件，应当在内核源码的arch/arm64/configs:\n"))
                os.system("mkdir patch")
                patch=int(input("需要为您的内核打补丁吗？\n1.需要。\n2.不需要。\n"))
                if patch == 1:
                    a=1
                    while a:
                        patchin=int(input("请将内核补丁放于同本脚本相同目录下的patch文件夹内！\n1.已放入。\n2.未放入。\n"))
                        if patchin == 1:
                            patchfilepath = "/root/patch"
                            os.system("cp -r /root/patch/* %s/"%(kerneldir))
                            for i,j,k in os.walk(patchfilepath):
                                for patchname in k :
                                    os.chdir("/root/%s"%(kerneldir))
                                    os.system("patch -p1 < %s"%(patchname))
                            a=0
                            os.chdir("/root")
                            os.system("export ARCH=arm64")
                            os.system("export SUBARCH=arm64")
                            os.system("export HEADER_ARCH=arm64")
                            os.system("make -C %s clean"%(kerneldir))
                            os.system("make -C %s mrproper"%(kerneldir))
                            os.system("make -C %s ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 %s"%(kerneldir,defconfig))
                            os.system("make -C %s ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 menuconfig"%(kerneldir))
                            defconfig_name=str(input("<你的配置名称(英文或数字)>_defconfig\n您想将配置保存为什么名称:\n"))
                            os.system("cp %s/.config %s/arch/arm64/configs/%s_defconfig"%(kerneldir,kerneldir,defconfig_name))
                            print("已将内核配置保存为%s_defconfig"%(defconfig_name))
                        else:
                            a=1
                            pass

                elif  patch == 2:
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C %s clean"%(kerneldir))
                    os.system("make -C %s mrproper"%(kerneldir))
                    os.system("make -C %s ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 %s"%(kerneldir,defconfig))
                    os.system("make -C %s ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 menuconfig"%(kerneldir))
                    defconfig_name=str(input("<你的配置名称(英文或数字)>_defconfig\n您想将配置保存为什么名称:\n"))
                    os.system("cp %s/.config %s/arch/arm64/configs/%s_defconfig"%(kerneldir,kerneldir,defconfig_name))
                    print("已将内核配置保存为%s_defconfig"%(defconfig_name))
                else:
                    print("没有这个选项")

            elif xuanzhe == 4:
                kerneldir=str(input("请输入您内核源码的压缩包或文件夹名称:\n"))
                defconfig = str(input("请输入您内核的配置文件，应当在内核源码的arch/arm64/configs:\n"))
                if ''.join(list(kerneldir)[-4:]) == ".zip":
                    kerneldir_1=''.join(list(kerneldir)[0:-4])
                    time_start=time.time()
                    os.system("unzip -d clang_make_kernel %s"%(kerneldir))
                    os.system("mv clang_make_kernel/* clang_make_kernel/%s"%(kerneldir_1))
                    #内核配置修改及环境配置：
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C clang_make_kernel/%s  O=../out/ ARCH=arm64 SUBARCH=arm64 CC=/root/tools/tc-build/installTmp/bin/clang LD=/root/tools/tc-build/installTmp/bin/ld.lld CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/tc-build/installTmp/bin/aarch64-linux-gnu- CROSS_COMPILE_ARM32=/root/tools/tc-build/installTmp/bin/arm-linux-gnueabi- %s"%(kerneldir_1,defconfig))
                    os.system("make -j%s -C clang_make_kernel/%s O=../out/ DTC_EXT=/root/tools/dtc-1.4.6/dtc ARCH=arm64 SUBARCH=arm64 CC=/root/tools/tc-build/installTmp/bin/clang LD=/root/tools/tc-build/installTmp/bin/ld.lld CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/tc-build/installTmp/bin/aarch64-linux-gnu- CROSS_COMPILE_ARM32=/root/tools/tc-build/installTmp/bin/arm-linux-gnueabi-"%(cpu_count(),kerneldir_1))
                    time_end=time.time()
                    usetime2=int(time_end-time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒"%(usetime2))
                else:
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C %s clean"%(kerneldir))
                    os.system("make -C %s mrproper"%(kerneldir))
                    os.system("rm -r %s/out/"%(kerneldir))
                    os.system("rm -r %s/../out"%(kerneldir))
                    time_start=time.time()
                    os.system("make -C %s  O=../out/ ARCH=arm64 SUBARCH=arm64 CC=/root/tools/tc-build/installTmp/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/tc-build/installTmp/bin/aarch64-linux-gnu- CROSS_COMPILE_ARM32=/root/tools/tc-build/installTmp/bin/arm-linux-gnueabi- %s"%(kerneldir,defconfig))
                    os.system("make -j%s -C %s O=../out/ DTC_EXT=/root/tools/dtc-1.4.6/dtc ARCH=arm64 SUBARCH=arm64 CC=/root/tools/tc-build/installTmp/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/tc-build/installTmp/bin/aarch64-linux-gnu- CROSS_COMPILE_ARM32=/root/tools/tc-build/installTmp/bin/arm-linux-gnueabi-"%(cpu_count(),kerneldir))
                    time_end=time.time()
                    usetime=int(time_end-time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒"%(usetime))

            elif xuanzhe == 5:
                kerneldir = str(input("请输入您内核源码的压缩包或文件夹名称:\n"))
                defconfig = str(input("请输入您内核的配置文件，应当在内核源码的arch/arm64/configs:\n"))
                android_versions = int(input("安卓内核务必和安卓系统相匹配否则无法编译或刷入后无法开机!!!!!\n请选择您的内核所属的安卓版本:\n1.Android6.x\n2.Android7.x\n3.Android8.x\n4.Android9.x\n5.Android10.x\n"))
                av = 1
                while av:
                    if android_versions == 1:
                        android_version = "marshmallow"
                        av = 0
                    elif android_versions == 2:
                        android_version = "nougat"
                        av = 0
                    elif android_versions == 3:
                        android_version = "oreo"
                        av = 0
                    elif android_versions == 4:
                        android_version = "pie"
                        av = 0
                    elif android_versions == 5:
                        android_version = "android10"
                        av = 0
                    else:
                        print("没有这个选项，请重新选择！！")
                        av = 1
                if ''.join(list(kerneldir)[-4:]) == ".zip":
                    kerneldir_1 = ''.join(list(kerneldir)[0:-4])
                    time_start = time.time()
                    os.system("unzip -d gcc_make_kernel %s" % (kerneldir))
                    os.system("mv gcc_make_kernel/* gcc_make_kernel/%s" % (kerneldir_1))
                    # 内核配置修改及环境配置：
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C gcc_make_kernel/%s  O=../out/ ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi- %s" % (kerneldir_1,android_version,android_version, defconfig))
                    os.system("make -j%s -C gcc_make_kernel/%s O=../out/ ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi-" % (cpu_count(),kerneldir_1,android_version,android_version))
                    time_end = time.time()
                    usetime3 = int(time_end - time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒"%(usetime3))
                else:
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C %s clean" % (kerneldir))
                    os.system("make -C %s mrproper" % (kerneldir))
                    os.system("rm -r %s/out/")
                    os.system("rm -r %s/../out")
                    time_start = time.time()
                    os.system("make -C %s  O=../out/ ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi- %s"%(kerneldir, android_version, android_version, defconfig))
                    os.system("make -j%s -C %s O=../out/ ARCH=arm64 SUBARCH=arm64 HEADER_ARCH=arm64 CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi-" %(cpu_count(), kerneldir, android_version, android_version))
                    time_end = time.time()
                    usetime4 = int(time_end - time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒" % (usetime4))

            elif xuanzhe == 6:
                print("正在下载工具链")
                os.system("git clone https://gitee.com/mao_zhifeng_admin/llvm-Snapdragon_LLVM_for_Android_8.0.git /root/tools/llvm-Snapdragon-android10")
                os.system("mv /root/tools/llvm-Snapdragon-android10/llvm-Snapdragon_LLVM_for_Android_8.0/prebuilt/linux-x86_64/* /root/tools/llvm-Snapdragon-android10/")
                os.system("rm -r /root/tools/llvm-Snapdragon-android10/llvm-Snapdragon_LLVM_for_Android_8.0/")
                os.system("git clone https://gitee.com/mao_zhifeng_admin/llvm-Snapdragon-6.0.9.git /root/tools/llvm-Snapdragon-pie")
                print("工具链下载完成！")

            elif xuanzhe == 7:
                kerneldir=str(input("请输入您内核源码的压缩包或文件夹名称:\n"))
                defconfig = str(input("请输入您内核的配置文件，应当在内核源码的arch/arm64/configs:\n"))
                android_versions = int(input("安卓内核务必和安卓系统相匹配否则无法编译或刷入后无法开机!!!!!\n请选择您的内核所属的安卓版本:\n1.Android6.x\n2.Android7.x\n3.Android8.x\n4.Android9.x\n5.Android10.x\n"))
                av = 1
                while av:
                    if android_versions == 1:
                        android_version = "marshmallow"
                        av = 0
                    elif android_versions == 2:
                        android_version = "nougat"
                        av = 0
                    elif android_versions == 3:
                        android_version = "oreo"
                        av = 0
                    elif android_versions == 4:
                        android_version = "pie"
                        av = 0
                    elif android_versions == 5:
                        android_version = "android10"
                        av = 0
                    else:
                        print("没有这个选项，请重新选择！！")
                        av = 1
                if ''.join(list(kerneldir)[-4:]) == ".zip":
                    kerneldir_1=''.join(list(kerneldir)[0:-4])
                    time_start=time.time()
                    os.system("unzip -d clang_make_kernel %s"%(kerneldir))
                    os.system("mv clang_make_kernel/* clang_make_kernel/%s"%(kerneldir_1))
                    #内核配置修改及环境配置：
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C clang_make_kernel/%s  O=../out/ ARCH=arm64 SUBARCH=arm64 CC=/root/tools/llvm-Snapdragon-%s/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi- %s"%(kerneldir_1,android_version,android_version,android_version,defconfig))
                    os.system("make -j%s -C clang_make_kernel/%s O=../out/ DTC_EXT=/root/tools/dtc-1.4.6/dtc ARCH=arm64 SUBARCH=arm64 CC=/root/tools/llvm-Snapdragon-%s/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi-"%(cpu_count(),kerneldir_1,android_version,android_version,android_version))
                    time_end=time.time()
                    usetime2=int(time_end-time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒"%(usetime2))
                else:
                    os.system("export ARCH=arm64")
                    os.system("export SUBARCH=arm64")
                    os.system("export HEADER_ARCH=arm64")
                    os.system("make -C %s clean"%(kerneldir))
                    os.system("make -C %s mrproper"%(kerneldir))
                    os.system("rm -r %s/out/"%(kerneldir))
                    os.system("rm -r %s/../out"%(kerneldir))
                    time_start=time.time()
                    os.system("make -C %s  O=../out/ ARCH=arm64 SUBARCH=arm64 CC=/root/tools/llvm-Snapdragon-%s/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi- %s"%(kerneldir,android_version,android_version,android_version,defconfig))
                    os.system("make -j%s -C %s O=../out/ DTC_EXT=/root/tools/dtc-1.4.6/dtc ARCH=arm64 SUBARCH=arm64 CC=/root/tools/llvm-Snapdragon-%s/bin/clang CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE=/root/tools/google-android-gcc/%s-aarch64/bin/aarch64-linux-android- CROSS_COMPILE_ARM32=/root/tools/google-android-gcc/%s-arm/bin/arm-linux-androideabi-"%(cpu_count(),kerneldir,android_version,android_version,android_version))
                    time_end=time.time()
                    usetime=int(time_end-time_start)
                    print("内核编译完成，请查看内核。本次编译耗时%s秒"%(usetime))

            elif xuanzhe == 8:
                os.system("git clone https://gitee.com/mao_zhifeng_admin/AnyKernel3.git  /root/tools/AnyKernel3")
                print("正在开发中，请等待..")
            else :
                print("没有这个选项，程序结束运行")
        else:
            print("脚本不在/root目录，正在移动，下次运行请去到/root/目录下！！")
            os.system("cp clang_gcc_make_kernel.py /root/")
            os.system("rm clang_gcc_make_kernel.py ")
            os.chdir("/root/")
            print("脚本已移至%s"%(os.getcwd()))
            os.system("python3 clang_gcc_make_kernel.py")
    else:
        print("系统不匹配，请使用AMD64架构的Ubuntu18及以上系统！！！！")
else:
    print("系统不匹配，请使用AMD64架构的Ubuntu18及以上系统！！！！")



