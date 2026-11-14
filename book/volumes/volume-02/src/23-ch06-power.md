# Power: Batteries, Wires and Heat

Every robot carries its own physics. The motors demand current, the wires resist it, the battery delivers what it can, and the difference between the three becomes heat. A design that ignores this arithmetic works beautifully on the bench for ten minutes and then behaves oddly, resets itself, or smells.

This chapter is about the three numbers that keep a robot alive: energy, current and temperature. It contains more arithmetic than any other chapter in the volume, and it is the one to read with a calculator.

## Energy Is What You Are Buying

A battery is a tank, and the size of the tank is measured in **watt-hours**: the power it can supply multiplied by the time it can supply it.

A pack labelled 11.1 V and 5 Ah holds 11.1 × 5 = 55.5 Wh. If the robot draws 5 A on average, that is 55.5 W, and the pack lasts about an hour in theory. In practice, perhaps 45 minutes, because batteries lose capacity at high discharge rates, the voltage sags as they empty, and running a pack flat shortens its life.

Work a realistic case. A small mobile robot has two drive motors drawing 3 A each when moving, a computer drawing 1.5 A, and sensors drawing 0.5 A. On a 22.2 V pack, the total current is 8 A, so the power is 178 W. For two hours of operation, the energy needed is 355 Wh, which means a pack of about 16 Ah at 22.2 V. That pack weighs roughly 1.5 kg and costs more than the motors.

Notice how quickly the numbers grow. A robot that must run all day either carries an enormous battery, docks and recharges, or follows a cable. There is no fourth option, which is why warehouse robots have charging stations in the aisles.

## The Three Numbers on a Battery

Every pack has three ratings, and all three matter.

**Voltage** sets the speed of the motors and must match the driver. A 24 V motor on a 12 V pack runs at about half speed and never reaches its rated power.

**Capacity** in amp-hours sets the runtime, as above. It is a rating at a particular discharge rate; a pack that gives 5 Ah at a gentle drain may give 4 Ah at a brutal one.

**C-rate** sets the maximum current. A 5 Ah pack rated at 20C can deliver 100 A briefly. Exceed it and the pack heats, sags, and in the case of lithium polymers, may ignite.

| Chemistry | Energy per kg | Cycle life | Notes |
|---|---|---|---|
| Lead-acid | 30–40 Wh/kg | 300–500 | Cheap, heavy, tolerant of abuse |
| Nickel-metal hydride | 60–120 Wh/kg | 500–1,000 | Robust, bulky, older technology |
| Lithium-ion | 150–250 Wh/kg | 500–2,000 | The default for robots, needs a battery manager |
| Lithium polymer | 150–250 Wh/kg | 300–1,000 | Same chemistry in a pouch, high current, fire risk |

Lithium packs require a **battery management system** that prevents overcharge, over-discharge and cell imbalance. A pack without one is a fire waiting for a reason. This is not a cautious aside; it is the single most common cause of serious damage in student robotics, and it happens when a pack is charged on the wrong setting, punctured, or discharged below its minimum.

## Wires Are Resistors

A wire is a resistor with good manners. It has a small resistance per metre, and when current flows through it the loss is given by

> power lost = current² × resistance

The square is the reason wire sizing surprises people. Doubling the current quadruples the loss. A wire that runs cool at 5 A can melt its insulation at 20 A, and it does so while the robot appears to work.

Take a copper wire of 0.75 mm² cross-section, which has a resistance of about 23 milliohms per metre. A drive motor 2 m from the battery needs 4 m of wire there and back, so 0.092 Ω. At 20 A, the loss is 400 × 0.092 = 37 W, spread along the wire, and the voltage drop is 20 × 0.092 = 1.84 V. On a 24 V system that is nearly 8% of the supply lost before the motor sees any of it.

Two consequences follow. Use thicker wire for high-current paths, and keep those paths short by putting the battery near the drivers. Both are free at the design stage and expensive afterwards.

| Current | Minimum sensible cross-section | Typical use |
|---|---|---|
| Up to 2 A | 0.2 mm² | Sensors, signals, small fans |
| 2–5 A | 0.5 mm² | Small motors, electronics |
| 5–15 A | 1.0 mm² | Drive motors on a small robot |
| 15–40 A | 2.5–4 mm² | Larger drives, robot arms |
| Above 40 A | 6 mm² and up | Traction, high-power arms |

## Fuses, Contactors and the Stop Button

A robot with a battery and no fuse has a single fault away from a fire. The fuse is not there to protect the electronics; it is there to protect the wire, which will otherwise glow before the electronics notice.

Protection is layered, and each layer does a different job.

The **fuse or breaker** limits the current a fault can draw, and it must be sized above the normal operating current and below the wire's rating.

The **contactor or main relay** allows the whole machine to be de-energised by a single command, which is what an emergency stop must do. A proper emergency stop cuts power to the actuators directly, not by asking the software nicely. Software can hang; a contactor cannot.

The **current limit in the driver** protects the motor from a stall that the fuse is too slow to catch.

The **thermal cut-out** protects the motor when it is working hard but not stalling — the slow case that fuses never see.

An emergency stop is a safety device and must be designed as one. It should be latching, so that restarting is a deliberate act; it should be reachable from where a person would stand; and it should be tested before the robot is used in front of anyone.

## Heat: The Quiet Killer

A motor converts electrical power into mechanical power and heat. The heat has to leave through the motor's surface, and the surface is small.

Return to the arm motor from the previous chapter, which needed 0.15 N·m at 314 rad/s. That is 47 W of mechanical output. At about 75% efficiency, the motor draws 63 W and produces 16 W of heat. A small motor has a thermal resistance to the surroundings of perhaps 3 K per watt, so 16 W gives a temperature rise of about 48 °C above ambient. In a 25 °C room, the winding reaches 73 °C — uncomfortable but survivable.

Now hold the arm against a stop, so the motor stalls at 24 A. The heat in the winding is hundreds of watts, the rise is hundreds of degrees, and the insulation fails in seconds. The fuse may not blow, because the current is within its rating for a short time. The encoder may survive; the motor will not.

The design response is a **duty cycle**: the fraction of time a machine may run at a given load. A motor rated for 50% duty can deliver its rated torque half the time and must rest the other half. A robot that lifts a heavy part once every ten seconds can use a motor that would overheat if it lifted continuously, and the datasheet will say so if you read past the first page.

## Problems

1. A pack is rated 14.8 V and 4 Ah. How much energy does it hold in watt-hours? If the robot draws 6 A, how long will it last in theory, and what would you expect in practice?

2. A wire of 1.0 mm² has a resistance of about 18 milliohms per metre. A motor draws 12 A through 3 m of wire (6 m round trip). Compute the power lost and the voltage drop. What fraction of a 24 V supply is lost?

3. Your robot needs 120 Wh per hour of operation and must run for four hours. What battery capacity in amp-hours do you need on a 22.2 V pack, and what mass would you expect?

4. A motor produces 30 W of heat and has a thermal resistance of 4 K/W. What temperature rise does it see? If the insulation is rated to 130 °C, what ambient temperature would make the design unsafe?

5. Write the four layers of electrical protection for a robot and, for each, the failure it prevents.
