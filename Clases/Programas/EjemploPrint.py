i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # campo minimo

print '"%5d"' % i      # field of width 5 characters/ campo de ancho 5 caracteres
print '"%05d"' % i     # pad with zeros  tablero con ceros

print '"%g"' % r       # r is big number so this is scientific notation   r es un gran numero entonces esta es la notacion cient
print '"%G"' % r       # E in the exponent  E en el exponente
print '"%e"' % r       # compact scientific notation
print '"%E"' % r       # compact scientific notation notacion cientifica compacta
print '"%20.2E"' % r   # 2 decimals, field of width 20
print '"%30g"' % r     # field of width 30 (right-adjusted)
print '"%-30g"' % r    # left-adjust number numero de ajuste a la izq
print '"%-30.4g"' % r  # 3 decimales

print '%s' % i   # can convert i to string automatically  puedo convertir i a cadena automaticamente
print '%s' % r

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
