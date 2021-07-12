salarioBase, horasExtras, bonificaciones = input().split()


vHoraNormal = float(salarioBase)/192
vHoraExtra = vHoraNormal + vHoraNormal*0.25
bonificacion = float(salarioBase) *0.05


if(bonificaciones == "0"):
    salario = float(salarioBase) + vHoraExtra*int(horasExtras)
    salarioTotal = salario - salario*0.085
    print(round(salarioTotal,1))

if(bonificaciones == "1"):
    salario = float(salarioBase) + vHoraExtra*int(horasExtras) + bonificacion
    salarioTotal = salario - salario*0.085
    print(round(salarioTotal,1))