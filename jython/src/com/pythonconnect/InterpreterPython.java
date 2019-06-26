package com.pythonconnect;

import org.python.util.PythonInterpreter;

public class InterpreterPython {
	public static void main(String[] args) {
//		System.setProperty("python.cachedir.skip", "true");
		PythonInterpreter interpreter = new PythonInterpreter();
		interpreter.exec("print(1)");
	}
}
