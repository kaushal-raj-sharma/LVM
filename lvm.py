import os

os.system("tput setaf 6")
print("\t\t\tWelcome to LVM Menu !!")

while(true):
    os.system("tput setaf 3")
    print("\n")
    print("******************************************************************************")
    print("\t\t\t1. To Configure A New LVM Storage ")
    print("\t\t\t2. To Increase The Size of LVM Storage")
    print("\t\t\t3. To Reduce the size of LVM Storage")
    print("\t\t\t4. To Mount The Newly Created Storage")
    print("\t\t\t5. To See All The Mounted Disk")
    print("\t\t\t6. To Display Volume Group")
    print("\t\t\t7. To Display Logical Volume")
    print("\t\t\t8. All Hard-Disk List Connected To System")
    print("\t\t\t9. Exit")
    print("*******************************************************************************")
    os.system("tput setaf 7")
    print("\n")
    
    a=int(input("ENTER YOUR OPTION : "))

    while(true):
        if(a==1):
            os.system("fdisk -l")
            num=int(input("Enter the number of hard-disk you want to join: "))
            num1=num
            l=[]
            while(num>0):
                c=input("Enter the storage name : ")
                l.append(c)
                num=num-1
            for i in range (0,num1):
                os.system("pvcreate {}".format(l[i]))
            print("physical volume created")
            vgname=input("Enter the volume group name: ")
            syntax=""
            for i in l:
                syntax+=i+" "
            os.system("vgcreate {} {}".format(vgname,syntax))
            print("volume group created")
            os.system("vgdisplay {}".format(vgname))
            print()
            lvmsize=int(input("Enter the logical volume size you want to create : "))
            lvmname=input("Enter the name of logical volume you want to keep : ")
            print("creating the logical volume of size-{} GIB with name- {}".format(lvmsize,lvmname))
            os.system("lvcreate --size {}G --name {} {}".format(lvmsize,lvmname,vgname))
            print("\t\t\tLVM of size-{}GB with name- {} created successfully".format(lvmsize,lvmname))
            os.system("lvdisplay")
            print()
            input("Press enter for LVM menu: ")
            break
        elif(a==2):
            
            vgname=input("Enter the name of Volume Group: ")
            lvname=input("Enter the name of logical volume group: ")
            os.system("vgdisplay {}".format(vgname))
            size=int(input("Enter the storage you want more in GB : "))

            os.system("lvextend --size +{}G /dev/{}/{}".format(size,vgname,lvname))
            os.system("resize2fs /dev/{}/{}".format(vgname,lvname))
            os.system("lvdisplay")
            print()
            print("\t\t\tSuccessfully Extended")
            os.system("df -h")
            input("Press enter to LVM menu: ")
            break
        elif(a==3): 
            vgname=input("Enter the name of volume group: ")
            lvname=input("Enter the name of logical volume group: ")
            mdir=input("Enter the mounted drive location: ")
            os.system("lvdisplay")
            size=int(input("Enter the size you actually want to reduce to : "))
            print("Unmounting the Logical Volume")
            os.system("umount /dev/{}/{}".format(vgname,lvname))
            os.system("e2fsck -f /dev/{}/{}".format(vgname,lvname))
            os.system("resize2fs /dev/{}/{} {}G".format(vgname,lvname,size))
            os.system("lvreduce -L {}G /dev/{}/{}".format(size,vgname,lvname))
            print("mounting the new shrinked volume to drive: {} ")
            os.system("mount /dev/{}/{} {}".format(vgname,lvname,mdir))
            os.system("lvdisplay")
            print("mounted shrinked volume: ")
            os.system("df -h")
            print()
            input("Press enter to main menu: ")
            break
        elif(a==4):
            dirname=input("Enter the name of mounting directory: ")
            os.system("mkdir /{}".format(dirname))
            print("{} Directory is Created".format(dirname))
            vgname=input("Enter the vgname: ")
            lvmname=input("Enter the LVMname: ")
            state=input("New lvm storage then press yes else no :")
            if(state=="yes"):
                os.system("fdisk /dev/{}/{}".format(vgname,lvmname))
                os.system("fdisk -l")
                dire=input("enter the directory: ")
                os.system("mkfs.ext4 {}".format(dire))

            os.system("mount /dev/{}/{} /{}".format(vgname,lvmname,dirname))
            print("Successfully Mounted")
            os.system("df -h")
            print()
            input("Press enter to LVM menu: ")
            break
        elif(a==5):
            os.system("df -h")
            input("Press enter to continue")
            break
        elif(a==6):
            os.system("vgdisplay")
            input("Press enter to continue")
            break
        elif(a==7):
            os.system("lvdisplay")
            input("Press enter to continue")
            break
        elif(a==8):
            os.system("fdisk -l")
            input("Press enter to continue")
            break
        elif(a==9):
            exit()