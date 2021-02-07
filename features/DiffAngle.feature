Feature: Different Angle

    "Açı2"'nin "Açı1"'e farkını hesaplar. Sonucu mutlak değeri en küçük olacak şekilde ayarlamalıdır.

    Scenario: Scenario name
        Given Angle1: 0
        When Angle2: 0
        Then Diff: 0

    # Scenario Outline: Zero Testi
    #     Given Angle1: <a1>
    #     When Angle2: <a2>
    #     Then Diff: <diff>

    #     Examples:
    #         | a1 | a2 | diff |
    #         | 0  | 0  | 0  |

        # Examples:
        #     | a1 | a2 | diff |
        #     | 0  | 0  | 0  |
        #     | 0 | 50  | 50  |
        #     | 0  | 180  | 180  |
        #     | 0 | 270  | -90  |

#     Scenario Outline: Basit Fark Testleri
#         """
#         Matematiksel olarak aralarındaki farkın kolayca hesaplanabildiği değerlerdir.
#         """
#         Given Angle1: <a1>
#         When Angle2: <a2>
#         Then Diff: <diff>

#         Examples:
#             | a1 | a2 | diff |
#             | 50 | 80  | 30  |
#             | 45 | 46  | 1  |
#             | 80 | 10  | -70  |
#             | -50  | 0  | 50  |
#             | -100  | -70  | 30  |
    
#     Scenario Outline: 180 Testi
#         Given Angle1: <a1>
#         When Angle2: <a2>
#         Then Diff: <diff>

#         Examples:
#             | a1 | a2 | diff |
#             | 0  | 180  | 180  |
#             | 30 | 210  | 180  |
#             | 30 | 210  | 180  |

#     Scenario Outline: Özel Durum Testleri
#         """
#         Matematiksel olarak çıkarma işlemiyle doğrudan hesaplanamayan değerlerdir.
#         """
#         Given Angle1: <a1>
#         When Angle2: <a2>
#         Then Diff: <diff>
    
#         Examples:
#             | a1 | a2 | diff |
#             | 350 | 10  | 20  |
#             | 0  | 270  | -90  |
#             | 180 | -270  | -90  |
