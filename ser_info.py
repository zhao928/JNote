import paramiko


ser_list = [
    '10.2.250.12',
    '10.2.250.13',
    '10.2.250.14',
    '10.2.250.15',
    '10.2.250.16',
    '10.2.250.17',
    '10.2.250.18',
    '10.2.250.19',
    '10.2.250.20',
    '10.2.250.21',
    '10.2.250.22',
    '10.2.250.23',
    '10.2.250.24',
    '10.2.250.25',
    '10.2.250.26',
    '10.2.250.27',
    '10.2.250.147',
    '10.2.250.148',
    '10.2.250.149',
    '10.2.250.150',
    '10.2.250.151',
    '10.2.250.152',
    '10.2.250.153',
    '10.2.250.154',
    '10.2.250.155',
    '10.2.250.156',
    '10.2.250.157',
    '10.2.250.158',
    '10.2.250.159',
    '10.2.250.160',
    '10.2.250.161',
    '10.2.250.162',
    '10.2.250.163',
    '10.2.250.164',
    '10.2.250.165',
    '10.2.250.166',
    '10.2.250.167',
    '10.2.250.28',
    '10.2.250.29',
    '10.2.250.30',
    '10.2.250.31',
    '10.2.250.32',
    '10.2.250.33',
    '10.2.250.34',
    '10.2.250.35',
    '10.2.250.36',
    '10.2.250.37',
    '10.2.250.90',
    '10.2.250.91',
    '10.2.250.92',
    '10.2.250.93',
    '10.2.250.94',
    '10.2.250.95',
    '10.2.250.109',
    '10.2.250.110',
    '10.2.250.111',
    '10.2.250.112',
    '10.2.250.113',
    '10.2.250.114',
    '10.2.250.115',
    '10.2.250.116',
    '10.2.250.117',
    '10.2.250.118',
    '10.2.250.119',
    ]


def ser_ssh(the_ser):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=the_ser, port=22, username="root", password="Jscm*dpi2022")
    cpu_in, cpu_out, cpu_err = ssh.exec_command("dmidecode -t processor|grep Version:")
    mem_in, mem_out, mem_err = ssh.exec_command("dmidecode|grep -A5 'Memory Device'|grep Size|grep -v Range")
    eth_in, eth_out, eth_err = ssh.exec_command("lspci |grep -i Ethernet")
    print(the_ser)
    cpu_all = cpu_out.read().decode()
    mem_all = mem_out.read().decode()
    eth_all = eth_out.read().decode()

    print(cpu_all.split('\n', 1)[1])

    mem_cunt = 0
    va = ''
    for v in mem_all.split('\n'):
        if 'GB' in v or 'MB' in v:
            mem_cunt += 1
            va = v
    print('\t', mem_cunt, '*', va.split(' ', 1)[1])

    for v in eth_all.split('\n'):
        print('\t', v.split(': ')[-1])

    ssh.close()


for i in ser_list:
    try:
        ser_ssh(i)
    except Exception as ser_err:
        print(i, ser_err)
