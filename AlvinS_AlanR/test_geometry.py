import geometry as geo

def test_point():
    point = geo.Point(2, 8)
    expected = 2
    actual = point.x
    assert expected == actual 
    expected = 8
    actual = point.y
    assert expected == actual 

def test_line_length():
    line = geo.Line(geo.Point(2, 8), geo.Point(5, 12))
    expected = 5
    actual = line.length
    assert expected == actual

def test_polyline():
    polyline = geo.Polyline()
    segment1 = geo.Line(geo.Point(1, 4), geo.Point(6, 10))
    segment2 = geo.Line(geo.Point(7, 2), geo.Point(3, 0))
    polyline.add_segment(segment1)
    polyline.add_segment(segment2)
    expected = 12.282385630906234
    actual = polyline.length
    assert expected == actual
