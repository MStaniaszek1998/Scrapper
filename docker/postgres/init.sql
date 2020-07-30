CREATE TABLE Statuses(
    STATUS_CODE numeric(10) primary key not null,
    STATUS_NAME varchar(100) null

);

INSERT INTO Statuses(STATUS_CODE, STATUS_NAME)
VALUES (0,'SUCCESS'), (1,'FAILURE');

CREATE TABLE URLS (
    URL varchar(2000) primary key not null,
    STATUS_CODE numeric(10) null REFERENCES Statuses(STATUS_CODE),
    CRAWLER varchar (100) not null,
    SCRAPE_TIME timestamp null,
    project varchar(200) not null
);



CREATE PROCEDURE insert_new_urls (
    url urls.url%TYPE,
    crawler urls.crawler%TYPE,
    project_name urls.project%TYPE,
    status_code urls.status_code%TYPE DEFAULT Null,
    SCRAPE_TIME urls.scrape_time%TYPE DEFAULT Null

)
language sql
as $$
    INSERT INTO URLS (URL,crawler,project,STATUS_CODE,SCRAPE_TIME)
    VALUES(url,crawler,project_name,status_code,SCRAPE_TIME)
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


CREATE FUNCTION fn_get_ieos(
    crawler_name URLS.crawler%TYPE
)
returns table(url urls.url%TYPE, project urls.project%TYPE)
    language sql
as
$$
SELECT url,project FROM URLS
WHERE CRAWLER=crawler_name and (STATUS_CODE is NULL  or STATUS_CODE !=0)
$$;

