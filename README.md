# PI PY

Archimedes algorithm to approximate PI.
I got the idea from Veritasium's video on ["The discovery that changed pi"](https://www.youtube.com/watch?v=gMlf1ELvRzc).

In it Dereck talks about the old intuitive algorithm, where you would subdivide the circle into finer and finer polygons, and apply Pythagoras' theorem to approximate PI.

I implemented it without looking at any code or algorithm online, just for fun. It gives pretty good approximations instantly, though you probably can't use it to get billions of digits of PI.

Here are the 100 first digits after 1k iterations (executed instantly): 
```txt
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117065
```
All the digits but the last seem to be correct.
