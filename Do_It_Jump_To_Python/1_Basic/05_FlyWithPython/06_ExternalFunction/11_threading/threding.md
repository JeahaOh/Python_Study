# threading
long_task()는 수행하는데 5초가 걸리는 함수다.  
예제는 이 함수를 5번 반복해서 수행하는 프로그햄이다.  
5초가 5번 반복되니 총 25초의 시간이 걸린다.  
```
01.py
```
  
스레드를 사용하면 5초의 시간이 걸리는 long_task()를 동시에 실행할 수 있으니 시간을 줄일 수 있다.  
```
02.py
```
  
threading.Thread()를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해주기 때문.  
  
하지만, START와 END가 먼저 출력되고,  
그 후에 스레드의 결과가 출력된다.  
START가 출력되고, 스레드의 결과가 출력된 후, END가 출력되도록 해보자.  
```
03.py
```
  
스레드의 join()는 해당 스레드가 종료될 때까지 기다리게 한다.