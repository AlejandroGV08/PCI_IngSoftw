import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EMIMIIB\SQLEXPRESS;DATABASE=Empresa;UID=sa;PWD=000000')

opc = "0"
while opc != "7":
    print("GESTION DE EMPRESA")
    print("1. Vendedores")
    print("2. Clientes")
    print("3. Articulos")
    print("4. Facturas")
    print("5. Municipios")
    print("6. Estados")
    print("7. Salir")
    opc = input("Seleccione una opcion: ") 
    cursorProductos = connection.cursor()
    
    if opc == "1":
        print("VENDEDORES")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Consultar")
        opc2 = input("Seleccione una opcion: ")
        print("ID: ")
        id_ven = input()
        
        if opc2 == "1": 
            print("Nombre: ")
            nombre = input() 
            print("Dirección: ")
            direccion = input() 
            print("Código Postal: ")
            cod_post = input() 
            print("ID de municipio: ")
            id_mun = input() 
            print("ID de estado: ")
            id_edo = input()    
            sql = "INSERT INTO vendedores (id_ven, nombre, direccion, cod_post, id_mun, id_edo) VALUES (?, ?, ?, ?, ?, ?)"
            val = (id_ven, nombre, direccion, cod_post, id_mun, id_edo)
            cursorProductos.execute(sql, val)        
            connection.commit()
            
        elif opc2 == "2":
            sql = "DELETE FROM vendedores WHERE id_ven = ?"
            cursorProductos.execute(sql, (id_ven,))
            connection.commit()
        
        elif opc2 == "3":
            print("Nombre: ")
            nombre = input() 
            print("Dirección: ")
            direccion = input() 
            print("Código Postal: ")
            cod_post = input() 
            print("ID de municipio: ")
            id_mun = input() 
            print("ID de estado: ")
            id_edo = input() 
            sql = "UPDATE vendedores SET nombre = ?, direccion = ?, cod_post = ?, id_mun = ?, id_edo = ? WHERE id_ven = ?"
            val = (nombre, direccion, cod_post, id_mun, id_edo, id_ven)
            cursorProductos.execute(sql, val)
            connection.commit()
            
        elif opc2 == "4":
            sql = "SELECT vendedores.id_ven, vendedores.nombre, vendedores.direccion, vendedores.cod_post, municipios.nombre, estados.nombre FROM vendedores INNER JOIN municipios ON municipios.id_mun = vendedores.id_mun INNER JOIN estados ON estados.id_edo = vendedores.id_edo WHERE id_ven = ?;"
            cursorProductos.execute(sql, (id_ven,))
            resultado = cursorProductos.fetchone()
            
            if resultado:
                print("", resultado)
            else:
                print("No se encontro el ID.")

        else:
            print("Opcion no valida")
            
    elif opc == "2":
        print("CLIENTES")
        print("1. Agregar")
        print("2. Modificar")
        print("3. Consultar")
        opc2 = input("Seleccione una opcion: ")
        print("ID: ")
        id_cli = input()
        
        if opc2 == "1": 
            print("Nombre: ")
            nombre = input() 
            print("Dirección: ")
            direccion = input() 
            print("Código Postal: ")
            cod_post = input() 
            print("ID de municipio: ")
            id_mun = input() 
            print("ID de estado: ")
            id_edo = input()    
            sql = "INSERT INTO clientes (id_cli, nombre, direccion, cod_post, id_mun, id_edo) VALUES (?, ?, ?, ?, ?, ?)"
            val = (id_cli, nombre, direccion, cod_post, id_mun, id_edo)
            cursorProductos.execute(sql, val)        
            connection.commit()
    
        elif opc2 == "2": 
            print("Nombre: ")
            nombre = input() 
            print("Dirección: ")
            direccion = input() 
            print("Código Postal: ")
            cod_post = input() 
            print("ID de municipio: ")
            id_mun = input() 
            print("ID de estado: ")
            id_edo = input() 
            sql = "UPDATE clientes SET nombre = ?, direccion = ?, cod_post = ?, id_mun = ?, id_edo = ? WHERE id_cli = ?"
            val = (nombre, direccion, cod_post, id_mun, id_edo, id_cli)
            cursorProductos.execute(sql, val)
            connection.commit()
            
        elif opc2 == "3":
            sql = "SELECT clientes.id_cli, clientes.nombre, clientes.direccion, clientes.cod_post, municipios.nombre, estados.nombre FROM clientes INNER JOIN municipios ON municipios.id_mun = clientes.id_mun INNER JOIN estados ON estados.id_edo = clientes.id_edo WHERE id_cli = ?;"
            cursorProductos.execute(sql, (id_cli,))
            resultado = cursorProductos.fetchone()
            
            if resultado:
                print("", resultado)
            else:
                print("No se encontro el ID.")

        else:
            print("Opcion no valida")
            
    elif opc == "3":
        print("ARTICULOS")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Modificar")
        print("4. Consultar")
        opc2 = input("Seleccione una opcion: ")
        print("ID: ")
        id_art = input()
        
        if opc2 == "1":
            print("Nombre: ")
            nombre = input() 
            print("Descripcion: ")
            descripcion = input() 
            print("Precio: ")
            precio = input() 
            print("Stock: ")
            stock = input() 
            print("Stock minimo: ")
            stock_min = input()    
            sql = "INSERT INTO articulos (id_art, nombre, descripcion, precio, stock, stock_min) VALUES (?, ?, ?, ?, ?, ?)"
            val = (id_art, nombre, descripcion, precio, stock, stock_min)
            cursorProductos.execute(sql, val)        
            connection.commit()
            
        elif opc2 == "2":
            sql = "DELETE FROM articulos WHERE id_art = ?"
            cursorProductos.execute(sql, (id_art,))
            connection.commit()
        
        elif opc2 == "3": 
            print("Nombre: ")
            nombre = input() 
            print("Descripcion: ")
            descripcion = input() 
            print("Precio: ")
            precio = input() 
            print("Stock: ")
            stock = input() 
            print("Stock minimo: ")
            stock_min = input() 
            sql = "UPDATE articulos SET nombre = ?, descripcion = ?, precio = ?, stock = ?, stock_min = ? WHERE id_art = ?"
            val = (id_art, nombre, descripcion, precio, stock, stock_min)
            cursorProductos.execute(sql, val)
            connection.commit()

        elif opc2 == "4":
            sql = "SELECT nombre, stock, stock_min FROM articulos WHERE id_art = ?;"
            cursorProductos.execute(sql, (id_art,))
            resultado = cursorProductos.fetchone()
            
            if resultado:
                print("", resultado)
            else:
                print("No se encontro el ID.")
                
        else:
            print("Opcion no valida")
            
    elif opc == "4":
        print("FACTURAS")
        print("1. Agregar")
        print("2. Modificar")
        print("3. Consultar")
        opc2 = input("Seleccione una opcion: ")
        print("ID: ")
        id_fac = input()
        
        if opc2 == "1":
            print("Fecha: ")
            fecha = input() 
            print("ID de articulo: ")
            id_art = input() 
            print("ID de cliente: ")
            id_cli = input() 
            print("ID de vendedor: ")
            id_ven = input() 
            print("IVA aplicado: ")
            iva = input()  
            print("Descuento aplicado: ")
            descuento = input()  
            sql = "INSERT INTO facturas (id_fac, fecha, id_art, id_cli, id_ven, iva, descuento) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (id_fac, fecha, id_art, id_cli, id_ven, iva, descuento)
            cursorProductos.execute(sql, val)        
            connection.commit()
    
        elif opc2 == "2":
            print("Fecha: ")
            fecha = input() 
            print("ID de articulo: ")
            id_art = input() 
            print("ID de cliente: ")
            id_cli = input() 
            print("ID de vendedor: ")
            id_ven = input() 
            print("IVA aplicado: ")
            iva = input()  
            print("Descuento aplicado: ")
            descuento = input()  
            sql = "UPDATE facturas SET fecha = ?, id_art = ?, id_cli = ?, id_ven = ?, iva = ?, descuento = ? WHERE id_fac = ?"
            val = (id_fac, fecha, id_art, id_cli, id_ven, iva, descuento)
            cursorProductos.execute(sql, val)
            connection.commit()
            
        elif opc2 == "3":
            sql = "SELECT facturas.id_fac, facturas.fecha, articulos.nombre, clientes.nombre, vendedores.nombre, facturas.iva, facturas.descuento FROM facturas INNER JOIN articulos ON facturas.id_art = articulos.id_art INNER JOIN clientes ON facturas.id_cli = clientes.id_cli INNER JOIN vendedores ON facturas.id_ven = vendedores.id_ven WHERE id_fac = ?;"
            cursorProductos.execute(sql, (id_fac,))
            resultado = cursorProductos.fetchone()
            
            if resultado:
                print("", resultado)
            else:
                print("No se encontro el ID.")

        else:
            print("Opcion no valida")
            
    elif opc == "5":
        print("MUNICIPIOS")
        print("1. Agregar")
        print("2. Consultar")
        opc2 = input("Seleccione una opcion: ")
        
        if opc2 == "1":
            print("ID del municipio: ")
            id_mun = input() 
            print("Nombre del municipio: ")
            nombre = input() 
            print("ID del estado: ")
            id_edo = input() 
            sql = "INSERT INTO municipios (id_mun, nombre, id_edo) VALUES (?, ?, ?)"
            val = (id_mun, nombre, id_edo)
            cursorProductos.execute(sql, val)        
            connection.commit()
            
        elif opc2 == "2":
            sql = "SELECT municipios.id_mun, municipios.nombre, estados.nombre FROM municipios INNER JOIN estados ON estados.id_edo = municipios.id_edo"
            cursorProductos.execute(sql)
            resultados = cursorProductos.fetchall()
            
            for resultado in resultados:
                print("", resultado)
                
        else:
            print("Opcion no valida")
            
    elif opc == "6":
        print("ESTADOS")
        print("1. Agregar")
        print("2. Consultar")
        opc2 = input("Seleccione una opcion: ")
        
        if opc2 == "1":
            print("ID del estado: ")
            id_edo = input() 
            print("Nombre del estado: ")
            nombre = input() 
            sql = "INSERT INTO estados (id_edo, nombre) VALUES (?, ?)"
            val = (id_edo, nombre)
            cursorProductos.execute(sql, val)        
            connection.commit()
            
        elif opc2 == "2":
            sql = "SELECT * FROM estados"
            cursorProductos.execute(sql)
            resultados = cursorProductos.fetchall()
            
            for resultado in resultados:
                print("", resultado)

    elif opc == "7":
        print("Saliendo del programa...")
        cursorProductos.close()