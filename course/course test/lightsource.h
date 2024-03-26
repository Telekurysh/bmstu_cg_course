#ifndef LIGHTSOURCE_H
#define LIGHTSOURCE_H

#include <QVector3D>
#include <QColor>

class LightSource
{
public:
    LightSource();  // Конструктор по умолчанию
    LightSource(const QVector3D& position, const QColor& color);  // Конструктор с параметрами

    // Геттеры и сеттеры для положения и цвета
    const QVector3D& getPosition() const;
    void setPosition(const QVector3D& position);

    const QColor& getColor() const;
    void setColor(const QColor& color);

private:
    QVector3D position;  // Положение источника света
    QColor color;        // Цвет источника света
};

#endif // LIGHTSOURCE_H
