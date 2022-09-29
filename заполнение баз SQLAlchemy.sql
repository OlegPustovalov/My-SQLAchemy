INSERT INTO publisher (id,name)
VALUES
(1,'Диалектика'),
(2,'Эксмо'),
(3,'БХВ Петербург'),
(4,'Microsoft Press');
INSERT INTO book (id,title,id_publisher)
VALUES
(1,'SQL за 10 минут',1),
(2,'Программирование на JAVA для начинающих',2),
(3,'Программирование на Android',3),
(4,'Upgrade Windows 10',4);
INSERT INTO shop  (id,name)
VALUES
(1,'Лабиринт'),
(2,'ОЗОН'),
(3,'Yandex market'),
(4,'WB'),
(5,'Амазон');
INSERT INTO stock  (id,id_book,id_shop,count)
VALUES
(1,1,1,10),
(2,1,2,20),
(3,2,1,25),
(4,2,2,30),
(5,3,4,35),
(6,4,5,100);
INSERT INTO sale  (id,price,date_sale,id_stock,count)
VALUES
(1,3,'11.09.22',1,5),
(2,3,'14.09.22',2,10),
(3,5,'15.09.22',3,15),
(4,5,'21.09.22',4,20),
(5,10,'23.09.22',5,15),
(6,20,'25.09.22',6,1);

--выборка магазинов по целевому издателю (Эксмо) через SQL
select sh.name from shop sh,stock st,book b,publisher p 
where p.id = b.id_publisher and b.id = st.id_book  and st.id_shop  = sh.id and p.name = 'Эксмо';


SELECT shop.id, shop.name, stock.id, stock.id_book, stock.id_shop, stock.count, book.id, book.title, book.id_publisher, publisher.id , publisher.name 
FROM shop, stock, book, publisher 
WHERE publisher.id = book.id_publisher AND book.id = stock.id_book AND stock.id_shop = shop.id AND publisher.name = 'Эксмо'

       


  
