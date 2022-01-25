import pytest
import Leccion1

def test_ingresoTotal():
    assert Leccion1.ingresoTotal()== 84349035.0

def test_gastoTotal():
    assert Leccion1.gastoTotal()== -92505485.0

def test_ColumnaVacia():
    assert Leccion1.comprobarColumnas()==False

def test_media():
    assert Leccion1.mediaValores()==-1319.1666666666667