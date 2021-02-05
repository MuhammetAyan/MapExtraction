Feature: LidarCenterPoint

    "LidarCenterPoint()" Lidar sinyallerinin robot üzerinden çıktığı noktanın haritaya göre koordinatlarını hesaplar.
    Lidar sinyalleri robotun ön kısmının tam ortasından çıktığı kabul edilir.

    Robotun konumu, robotun tam merkez noktası kabul edilir.


    Scenario: Zero Test
        Given Robot position: (0, 0), angle: 0
        When Robot size: (50, 20)
        Then Center point: (25, 0)
    
    Scenario: Zero Test - Big Size
        Given Robot position: (0, 0), angle: 0
        When Robot size: (100, 50)
        Then Center point: (50, 0)
    
    Scenario: Different Position
        Given Robot position: (23, 35), angle: 0
        When Robot size: (50, 20)
        Then Center point: (48, 35)
    
    Scenario: Different Position (2)
        Given Robot position: (53, 68), angle: 0
        When Robot size: (50, 20)
        Then Center point: (78, 68)
    
    Scenario: Different Position - Big Size
        Given Robot position: (53, 400), angle: 0
        When Robot size: (150, 60)
        Then Center point: (128, 400)
    
    Scenario: Different Direction - Zero Test - 90
        Given Robot position: (0, 0), angle: 90
        When Robot size: (50, 20)
        Then Center point: (0, 25)
    
    Scenario: Different Direction - Zero Test - 180
        Given Robot position: (0, 0), angle: 180
        When Robot size: (50, 20)
        Then Center point: (-25, 0)
    
    Scenario: Different Direction - Zero Test - -90
        Given Robot position: (0, 0), angle: -90
        When Robot size: (50, 20)
        Then Center point: (0, -25)
    
    Scenario: Different Direction - Zero Test - 45
        Given Robot position: (0, 0), angle: 45
        When Robot size: (50, 20)
        Then Center point: (18, 18)
    
    Scenario: Different Direction - Zero Test - 25
        Given Robot position: (0, 0), angle: 25
        When Robot size: (50, 20)
        Then Center point: (23, 11)
    
    Scenario: Different Direction - Big Size - 90
        Given Robot position: (0, 0), angle: 90
        When Robot size: (76, 35)
        Then Center point: (0, 38)
    
    Scenario: Different Direction - Odd Size - 90
        Given Robot position: (0, 0), angle: 90
        When Robot size: (75, 35)
        Then Center point: (0, 37)
    
    Scenario: Different Direction - Big Size - 50
        Given Robot position: (0, 0), angle: 50
        When Robot size: (160, 60)
        Then Center point: (51, 61)
    
    Scenario: Different Position And Direction - 90
        Given Robot position: (50, 68), angle: 90
        When Robot size: (76, 35)
        Then Center point: (50, 106)
    
    Scenario: Different Position And Direction - 53
        Given Robot position: (43, -50), angle: 53
        When Robot size: (56, 89)
        Then Center point: (60, -28)
    
    Scenario: Different Position And Direction - Negatif Angle - -50
        Given Robot position: (50, 150), angle: -50
        When Robot size: (100, 30)
        Then Center point: (82, 112)