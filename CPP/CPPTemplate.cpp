#include <iostream>
#include <string>

// 面向对象部分
class Person {
public:
    Person(std::string name, int age) : name(name), age(age) {}

    void introduce() const {
        std::cout << "我叫" << name << "，今年" << age << "岁。" << std::endl;
    }

    void haveBirthday() {
        age++;
        std::cout << "今天是我的生日，我现在" << age << "岁了！" << std::endl;
    }

private:
    std::string name;
    int age;
};

// 面向过程部分
void greet(const std::string& name) {
    std::cout << "你好，" << name << "！欢迎来到这里。" << std::endl;
}

int main() {
    // 使用面向对象部分
    Person person("张三", 30);
    person.introduce();
    person.haveBirthday();

    // 使用面向过程部分
    greet(person.getName()); // 假设Person类有一个getName方法

    return 0;
}
