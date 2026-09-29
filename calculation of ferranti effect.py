import math

 Input values
Vs = float(input("Enter sending-end voltage (kV): "))
beta = float(input("Enter phase constant (rad/km): "))
length = float(input("Enter transmission line length (km): "))

Calculate beta*l
angle = beta * length

Calculate receiving-end voltage
Vr = Vs / math.cos(angle)

 Calculate Ferranti effect
ferranti_effect = ((Vr - Vs) / Vs) * 100

 Display results
print("\n--- Ferranti Effect Calculation ---")
print("Sending-end voltage =", Vs, "kV")
print("Line length =", length, "km")
print("Phase constant =", beta, "rad/km")
print("Receiving-end voltage =", round(Vr, 3), "kV")
print("Ferranti Effect =", round(ferranti_effect, 2), "%")
