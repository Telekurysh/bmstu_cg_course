#include "lightsource.h"

LightSource::LightSource()
    : position(QVector3D(0, 0, 0)), color(Qt::white)
{
}

LightSource::LightSource(const QVector3D& position, const QColor& color)
    : position(position), color(color)
{
}

const QVector3D& LightSource::getPosition() const
{
    return position;
}

void LightSource::setPosition(const QVector3D& position)
{
    this->position = position;
}

const QColor& LightSource::getColor() const
{
    return color;
}

void LightSource::setColor(const QColor& color)
{
    this->color = color;
}
