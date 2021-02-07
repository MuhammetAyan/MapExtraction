Feature: Robotu hedefe sürme

    "Arrival_to_goal()" fonksiyonu, mouse ile bir konuma tıklatılınca robotun o konuma gitmesini sağlar.

    Robotun konumu, robotun tam merkez noktası kabul edilir.
    Robotun hedefe varıp varmadığını ve doğru dönüş yapıp yapmadığı kontrol edilecektir.

    Background:
        Given Robot position: (0, 0)
        And Angle: 0

    
    Scenario: Robotun bulunduğu konumun hedef olarak gösterilmesi
        When Mouse ile (0, 0) noktasına tıklanınca
        Then Hedef varış durumu: "True". Açı değişme durumu: "yok"
    
    Scenario: Robotun bulunduğu konumun hedef olarak gösterilmesi - 2
        Given Robot position: (58, 63)
        When Mouse ile (58, 63) noktasına tıklanınca
        Then Hedef varış durumu: "True". Açı değişme durumu: "yok"

    Scenario: Robotun bulunduğu konumun hedef olarak gösterilmesi - 3
        Given Robot position: (58, 63)
        And Angle: 57
        When Mouse ile (58, 63) noktasına tıklanınca
        Then Hedef varış durumu: "True". Açı değişme durumu: "yok"
    
    Scenario: Robotun önündeki bir noktanın hedef tayin edilmesi - 0
        When Mouse ile (100, 0) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "yok"
    
    Scenario: Robotun önündeki bir noktanın hedef tayin edilmesi - 90
        Given Robot position: (100, 0)
        And Angle: 90
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "yok"

    Scenario: Robotun önündeki bir noktanın hedef tayin edilmesi - 180
        Given Robot position: (100, 0)
        And Angle: 180
        When Mouse ile (0, 0) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "yok"
    
    Scenario: Robotun önündeki bir noktanın hedef tayin edilmesi - 45
        Given Angle: 45
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "yok"

    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - 0
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonu"
    
    # Bu senaryo fail alıyor
    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - -180
        Given Angle: -180
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonunun tersi"
    
    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - 180
        Given Angle: 180
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonunun tersi"

    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - 200
        Given Angle: 200
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonunun tersi"
    
    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - robot orjinde değil
        Given Robot position: (150, 100)
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonu"
    
    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - robotun ile hedef açısı 1 derece
        Given Robot position: (150, 100)
        And Angle: 181
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonunun tersi"
    
    Scenario: Robotun bakmadığı bir noktanın hedef tayin edilmesi - robotun ile hedef açısı -1 derece
        Given Robot position: (150, 100)
        And Angle: 179
        When Mouse ile (100, 100) noktasına tıklanınca
        Then Hedef varış durumu: "False". Açı değişme durumu: "saat yonu"
    
    