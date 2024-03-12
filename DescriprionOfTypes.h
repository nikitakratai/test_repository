// it's a file which contains description of add used types;

struct wheel:
{
 diameter: real;
 isVoronenied: bool;
}

struct t_car:
{
 weight, length, height, width: double;
 color: TColor;
 w1, w2, w3, w4: wheel;
}

struct cortage:
{
 num: integer;
 cars:t_car[num];
}
