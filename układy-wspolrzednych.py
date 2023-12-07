import math
def wspolrzedne_kartezjanskie():
    try:
        x = float(input("Podaj pierwszą wartość \"x\": "))
        y = float(input("Podaj drugą wartość \"y\" : "))
        z = float(input("Podaj trzecią wartość \"z\" : "))
        return x, y, z
    except ValueError:
        print("Spróbuj ponownie!")
        return wspolrzedne_kartezjanskie()
def kart_do_sferycznego(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    if r == 0:
        return r,0,0
    theta = math.acos(z / r)
    phi = math.atan2(y, x)
    return r, theta, phi

def kart_do_cylindrycznego(x, y, z):
    r_c = math.sqrt(x**2 + y**2)
    theta_c = math.atan2(y, x)
    z_cy = z
    return r_c, theta_c, z_cy

if __name__ == "__main__":
    x, y, z = wspolrzedne_kartezjanskie()

    r_sf, theta_sf, phi_sf = kart_do_sferycznego(x, y, z)
    print("Współrzedne sferyczne: ","r = ", r_sf ," , ","θ = ", theta_sf," , ","ϕ = ", phi_sf)
    r_cy, theta_cy, z_cy = kart_do_cylindrycznego(x, y, z)
    print("Współrzedne cylindryczne: ","rc = ", r_cy," , ","θc = ", theta_cy," , ","Zc = ", z_cy)
