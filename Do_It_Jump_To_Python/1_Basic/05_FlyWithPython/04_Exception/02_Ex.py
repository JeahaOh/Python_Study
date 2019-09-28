# coding: utf-8
try:
  4 / 0
except ZeroDivisionError as e:
  print( e )

try:
  a = [1, 2]
  print( a[3] )
  4 / 0
except ZeroDivisionError:
  print( 'Can not Divid by 0.' )
except IndexError:
  print( 'Can not Find Index.' )

try:
  a = [1, 2]
  print( a[3] )
  4 / 0
except ZeroDivisionError as e:
  print( e )
except IndexError as e:
  print( e )

try:
  4 / 0
  a = [1, 2]
  print( a[3] )
except (ZeroDivisionError, IndexError) as e:
  print( e )

