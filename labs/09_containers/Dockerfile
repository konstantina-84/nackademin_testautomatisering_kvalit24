#En officiell Python 3.9-image som innehåller allt som behövs för att köra Python-program.
FROM python:3.9

#Sätter arbetskatalogen inne i containern till /test
WORKDIR /test

#Installerar testverktyg pytest-playwright, playwright och webbläsare(såsom Chromiun,Firefox), samt nödvändiga beroenden. 
RUN pip install --no-cache-dir --upgrade pytest-playwright
RUN playwright install --with-deps

#Flyttar min lokala testfil(test_home.py) in i containern, till arbetskatalogen /test.
COPY ./test_home.py /test/

#När containern körs, startar den pytest och kör testet i test_home.py.
CMD ["pytest", "./test_home.py"]