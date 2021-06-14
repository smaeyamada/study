import numpy as np

def Hubeny(lat0, lon0, lat1, lon1):
    """ 距離[m]算出 """
    Dy = (lat1 - lat0) * np.pi/180    # 2点の緯度(ラジアン)の差
    Dx = (lon1 - lon0) * np.pi/180    # 2点の軽度(ラジアン)の差
#     P = np.mean([lat0, lat1])
    P = np.mean([lat0, lat1], axis=0)    # 配列用 debug
    Rx = 6378137.000        # WGS84 長半径(赤道半径)
    Ry = 6356752.314245     # WGS84 短半径(極半径)
    
    E = np.sqrt((Rx**2 - Ry**2) / Rx**2)    # 離心率
    W = np.sqrt(1-(E**2)*((np.sin(P))**2))
    M = Rx*(1-(E**2)) / W**3    # 子午線曲率半径
    N = Rx / W                  # 卯酉線曲率半径
    D = np.sqrt(((Dy*M)**2) + ((Dx*N*np.cos(P))**2))
    return D


POLE_RADIUS = 6356752    # 極半径(短半径)
EQUATOR_RADIUS = 6378137 # 赤道半径(長半径)
E = 0.081819191042815790 # 離心率
E2= 0.006694380022900788 # 離心率の２乗

def Hubeny2(lat0, lon0, lat1, lon1):
    a_rad_lat = np.radians(lat0)
    a_rad_lon = np.radians(lon0)
    b_rad_lat = np.radians(lat1)
    b_rad_lon = np.radians(lon1)
    m_lat = (a_rad_lat + b_rad_lat) / 2 # 平均緯度
    d_lat = a_rad_lat - b_rad_lat # 緯度差
    d_lon = a_rad_lon - b_rad_lon # 経度差
    W = np.sqrt(1 - E2 * np.power(np.sin(m_lat), 2))
    M = EQUATOR_RADIUS * (1 - E2) / np.power(W, 3) # 子午線曲率半径
    N = EQUATOR_RADIUS / W # 卯酉線曲率半径
    d = np.sqrt(np.power(M * d_lat, 2) + np.power(N * d_lon * np.cos(m_lat), 2))
    return d
