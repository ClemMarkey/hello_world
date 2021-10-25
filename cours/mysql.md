# Definition d'une classe gérant la configuration permettant la connection à un serveur mysql

```
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='beer',
        port='3307'
    )

    conn.autocommit = True
```

conn est un attribut créé pour stocker la connection à mysql

---

### **Les paramètres**

_host_ : lieu ou est hebergé le serveur

_user_ : compte se connectant au serveur

_password_ : mot de passe du compte

_database_ : nom de la base de données

_port_ : système permettant la communication avec mysql

---

### **Communication avec la base de données**

`cursor = Connect.conn.cursor()`

le curseur permet d'executer des instructions pour communiquer avec la base de données MySQL
