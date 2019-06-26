package com.pythonconnect;

import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class BuildingFactory {

    private PyObject buildingClass;

    /**
     * 새 PythonInterpreter 개체를 생성한 다음, 파이썬
     * 코드를 실행하는 데에 사용. 이 경우, 강제 변형할
     * 파이썬 모듈을 수입한다.
     *
     * 일단 모듈이 수입되면 그에 대한 참조를 얻어서 자바
     * 변수에 참조를 할당한다
     */

    public BuildingFactory() {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("from Building import Building");
        buildingClass = interpreter.get("Building");
    }

    /**
     * create 메소드는 참조되는 파이썬 모듈을 자바 바이트코드로
     * 실질적인 강제 변형을 수행할 책임이 있다
     */

    public BuildingType create (String name, String location, String id) {

        PyObject buildingObject = buildingClass.__call__(new PyString(name),
                                                         new PyString(location),
                                                         new PyString(id));
        return (BuildingType)buildingObject.__tojava__(BuildingType.class);
    }

}
