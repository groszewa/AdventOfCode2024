CXX = clang++
CXXFLAGS = -std=c++2a -Wall -Wextra

TARGET = d1p2.exe

all: $(TARGET)

$(TARGET): main.cpp
	$(CXX) $(CXXFLAGS) main.cpp -o $(TARGET)

clean:
	rm -f $(TARGET)
