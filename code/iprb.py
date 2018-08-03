def main():
    dom = 28
    het = 15
    rec = 22

    tot = float(dom + het + rec)
    
    prob = 1-(rec/tot)*((rec-1)/(tot-1)) - (rec/tot)*(het/(tot-1)) - (het/tot)*((het-1)/(tot-1))*0.25

    print(prob)

if __name__ == "__main__":
    main()
