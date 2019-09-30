# tmepfile
파일을 임시로 만들어서 사용할 때 쓰는 모듈.
`tempfile.mktemp()`는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 반환.

```
>>> import tempfile
>>> filename = tempfile.mktemp()
>>> filename
'/var/folders/d5/5mt1rd2s1_sg3kqjymfxmg4h0000gn/T/tmpeyxCZD'
```

`tempfile.TemporaryFile()`은 임시 저장 공간으로 사용할 파일 객체를 반환한다.  
이 파일은 기본적으로 바이너리 쓰기모드(wb)를 갖는다.  
`close()`를 호출하면 이 파일 객체는 사라진다.  

```
>>> import tempfile
>>> f = tempfile.TemporaryFile()
>>> f.close()
```