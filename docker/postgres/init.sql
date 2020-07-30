CREATE TABLE Statuses(
    STATUS_CODE numeric(10) primary key not null,
    STATUS_NAME varchar(100) null

);

INSERT INTO Statuses(STATUS_CODE, STATUS_NAME)
VALUES (0,'SUCCESS'), (1,'FAILURE');

CREATE TABLE URLS (
    URL varchar(2000) primary key not null,
    STATUS_CODE numeric(10) null REFERENCES Statuses(STATUS_CODE),
    SCRAPE_TIME timestamp null
);



CREATE PROCEDURE insert_new_urls (
    url urls.url%TYPE,
    status_code urls.status_code%TYPE DEFAULT Null,
    SCRAPE_TIME urls.scrape_time%TYPE DEFAULT Null

)
language sql
as $$
    INSERT INTO URLS (URL,STATUS_CODE,SCRAPE_TIME)
    VALUES(url,status_code,SCRAPE_TIME)
$$;


CREATE PROCEDURE update_urls (
    url_a urls.url%TYPE,
    status_code_a urls.status_code%TYPE ,
    SCRAPE_TIME_a urls.scrape_time%TYPE

)
language sql
as $$

    UPDATE urls
    set status_code=status_code_a,scrape_time=SCRAPE_TIME_a
    where url=url_a

$$;




